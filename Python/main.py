from fastapi import FastAPI
from prophet import Prophet
import pandas as pd
import datetime as dt
from pydantic import BaseModel
from json import loads

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
               periods=7,
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
        result = forecast.tail(periods)
        result.reset_index(drop=True, inplace=True)
        result['ds'] = result['ds'].dt.strftime('%Y-%m-%d')
        result = result[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
        return loads(result.to_json(orient="records"))
    except Exception as e:
        print(str(e))
    return None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/predict/weekly/{city}")
async def predict_weekly(city: str):
    return load_model(city)
