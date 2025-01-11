import tweepy
from dotenv import load_dotenv
import os

class Tweet_Factory():
        
        def __init__(self, access_token, access_token_secret):
            self.client = tweepy.Client(
                        consumer_key= os.getenv("API_KEY"),
                        consumer_secret= os.getenv("API_SECRET"),
                        access_token= access_token,
                        access_token_secret= access_token_secret
                    )
        def create_tweet(self, tweet):     
            self.client.create_tweet(text = tweet)
