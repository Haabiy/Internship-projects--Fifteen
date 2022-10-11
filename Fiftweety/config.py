import tweepy
import logging
from slack_sdk import WebClient

# Consumer keys
API_Consumer_KEY = ''
API_Consumer_Key_Secret = ''

# API authentication keys
Bearer_Token = ''
Access_Token = ''
Access_Token_Secret = ''
logger = logging.getLogger()

# Slack API
SLACK_API = WebClient(token=(''))
#print(SLACK_API.api_test())

def create_api():
    auth = tweepy.OAuthHandler(API_Consumer_KEY, API_Consumer_Key_Secret)
    auth.set_access_token(Access_Token, Access_Token_Secret)
    api = tweepy.API(auth, wait_on_rate_limit=False)
    # making sure we can access my Twitter account
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
