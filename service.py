import tweepy
from secretsKeys import ACCESS_TOKEN
from secretsKeys import ACCESS_TOKEN_SECRET
from secretsKeys import API_KEY
from secretsKeys import API_SECRET_KEY
from secretsKeys import BEARER_TOKEN
from typing import List
from typing import Any
from typing import Dict

def get_trends(woe_id: int) -> List[Dict[str, Any]]:

    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = api.get_place_trends(woe_id)    

    return [trend for trend in trends]