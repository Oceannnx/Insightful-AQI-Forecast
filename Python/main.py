from fastapi import FastAPI
from prophet import Prophet
import pandas as pd
import datetime as dt
from pydantic import BaseModel

app = FastAPI()

def now():
    return dt.datetime.now()

class Item(BaseModel):
    year: str
    month: str
    day: str
    periods: int
    type: str

def load_model(city,
               year=now().strftime('%Y'),
               month=now().strftime('%m'),
               day=now().strftime('%m'),
               periods=30,
               type='pm25'):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
        periods = int(periods)
        data = pd.read_csv(f'..\\resource\\{city}-air-quality.csv', parse_dates=['date'], skipinitialspace=True)
        data = data.sort_index()
        y_col = type
        data.dropna(subset=[y_col], inplace=True)
        df = data[['date', y_col]]
        df.columns = ['ds', 'y']
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=(periods))
        forecast = model.predict(future)
        result = forecast[forecast['ds'] == dt.datetime(year, month, day)]
        result.reset_index(drop=True, inplace=True)
        return result[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    except Exception as e:
        print(str(e))
    return None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/ai/{city}")
async def read_item(city: str, req: Item):
    return load_model(city, req.year, req.month, req.day, req.periods, req.type)

# @app.get("/api/ai/{city}")
# async def read_item(city: str):
#     return load_model(city);