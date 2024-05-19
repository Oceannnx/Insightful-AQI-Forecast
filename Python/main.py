from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prophet import Prophet
import pandas as pd
import datetime as dt
from pydantic import BaseModel
from json import loads

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}

def now():
    return dt.datetime.now()

class Item(BaseModel):
    year: str
    month: str
    day: str
    periods: int
    type: str

def load_model(city,
                start=now(),
                end=now() + dt.timedelta(days=7),
                type='pm25'
                ):
    try:
        periods = (end - start).days
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
        result = forecast[(forecast['ds'] >= dt.datetime(start.year, start.month, start.day))]
        result = result[forecast['ds'] <= dt.datetime(end.year, end.month, end.day)]
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

@app.get("/predict/range/{city}/{start}/{end}")
async def predict_range(city: str, start: str, end: str):
    return load_model(city, start=dt.datetime.strptime(start, '%Y-%m-%d'), end=dt.datetime.strptime(end, '%Y-%m-%d'))