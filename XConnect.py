import tweepy
from dotenv import load_dotenv
import os

class X_Connect:

    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv("API_KEY")
        self.API_SECRET = os.getenv("API_SECRET")
        self.oauth1_user_handler = tweepy.OAuth1UserHandler(
            self.API_KEY, self.API_SECRET,
            callback="http://127.0.0.1:5000/xverification"
        )

    def get_url(self):
        return self.oauth1_user_handler.get_authorization_url()
    
    

    def get_tokens(self, verifier):
        access_token, access_token_secret = self.oauth1_user_handler.get_access_token(verifier)
        return(access_token, access_token_secret)


