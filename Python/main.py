from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prophet import Prophet
import pandas as pd
import datetime as dt
import pymongo
import requests
from json import loads
from dotenv import load_dotenv
import os


app = FastAPI()

load_dotenv()

MONGODB_URL = os.getenv('MONGODB_URL')

client = pymongo.MongoClient(MONGODB_URL)
db = client.get_database('InsightfulAqiForecast')

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
    "https://insightful-aqi-forecast-8rx92cz0f-oceannnxs-projects.vercel.app/",
    "https://insightful-aqi-forecast-hh3p96m2g-oceannnxs-projects.vercel.app/",
    "https://insightful-aqi-forecast-git-main-oceannnxs-projects.vercel.app/",
    "https://insightful-aqi-forecast-oceannnxs-projects.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def now():
    return dt.datetime.now()

def load_model(city,
                start=now(),
                end=now() + dt.timedelta(days=7),
                type='pm25'
                ):
    try:
        periods = (end - now()).days +1
        periods = int(periods)
        city = city.lower()
        addDataToDB(city)
        data = fetchDataFromDB(city)
        y_col = type
        data.dropna(subset=[y_col], inplace=True)
        df = data[['date', y_col]]
        df.columns = ['ds', 'y']
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=(periods))
        forecast = model.predict(future)
        result = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
        result = result[result['ds'] >= start]
        result = result[result['ds'] <= end]
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
    return load_model(city.lower(), start=dt.datetime.strptime(start, '%Y-%m-%d'), end=dt.datetime.strptime(end, '%Y-%m-%d'))

@app.get("/history/{city}/{year}")
async def history(city: str, year: str):
    try:
        city = city.lower()
        addDataToDB(city)
        data = fetchDataFromDB(city)
        data = data.sort_index()
        data['date'] = data['date'].dt.strftime('%Y-%m-%d')
        data = data[data['date'].str.contains(year)]
        data.reset_index(drop=True, inplace=True)
        data = data.sort_values(by='date')
        return loads(data.to_json(orient="records"))
    except Exception as e:
        print(str(e))
    return None

def addDataToDB(city:str):
    try:
        city.lower()
        collection = db[city]
        find = collection.find_one({"date":dt.datetime.now().strftime('%Y-%m-%d')})
        if find:
            return False
        result = requests.get(f'https://api.waqi.info/feed/{city}/?token=3ad15d8e229a5120ed11e38c946922b0b9a42ac7')
        result = result.json()
        date = dt.datetime.now().strftime('%Y-%m-%d')
        pm25 = result['data']['iaqi']['pm25']['v']
        pm10 = result['data']['iaqi']['pm10']['v']
        o3 = result['data']['iaqi']['o3']['v']
        no2 = result['data']['iaqi']['no2']['v']
        so2 = result['data']['iaqi']['so2']['v']
        Data = {
            "date":date,
            "pm25":pm25,
            "pm10":pm10,
            "o3":o3,
            "no2":no2,
            "so2":so2
        }
        collection.insert_one(Data)
    except Exception as e:
        print(str(e))

def fetchDataFromDB(city:str):
    try:
        city.lower()
        collection = db[city]
        data = collection.find()
        df = pd.DataFrame(list(data))
        df.drop(columns=['_id'], inplace=True)
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by='date')
        return df
    except Exception as e:
        print(str(e))
    return None

@app.get("/test")
async def test():
    addDataToDB('bangkok')
    return fetchDataFromDB('bangkok')