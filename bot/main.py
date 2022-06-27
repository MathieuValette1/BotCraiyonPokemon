import tweepy
import json
from os import environ

API_KEY = environ['API_KEY']
API_SECRET_KEY = environ['API_SECRET_KEY']

ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

def create_tweet():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    tweet = 'Hello Twitter'
    api.update_status(tweet)

    return tweet




def lambda_handler(event, context):

    result = create_tweet()

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }