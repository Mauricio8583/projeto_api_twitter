from secretsKeys import ACCESS_TOKEN
from secretsKeys import ACCESS_TOKEN_SECRET
from secretsKeys import API_KEY
from secretsKeys import API_SECRET_KEY
from fastapi import FastAPI
from service import get_trends
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List
import tweepy
import uvicorn

BRAZIL_WOE_ID = 23424768

client = MongoClient("mongodb://dio:dio@localhost:27017/")

db = client.my_test

tweets_collection = db.tweets_collection

tweets_collection.insert_one({"author": "test", "text": "Texto qualquer"})

tweets = tweets_collection.find({})

print(list(tweets))

app = FastAPI()

class trendItem(BaseModel):
    name: str
    url: str

@app.get("/trends", response_model=List[trendItem])
def get_trends_route():

    trends = get_trends(BRAZIL_WOE_ID)

    return trends["trends"]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)