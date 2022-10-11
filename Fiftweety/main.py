from config import SLACK_API
from config import create_api
import pandas as pd
import numpy as np
import datetime
import re


# 1. Authentication comes first
# create_api() returns api
api = create_api()
user_ = create_api().get_user(screen_name='haabiy')
#print('Name : ', user_.name)
#print('ID :', user_.id)
print('______')
print('Initiating Fiftweety...')
# I'll use set of targeted Twitter accounts
#file = open("Twitter - Public twitter accounts.csv", encoding='latin-1')
#dff = pd.read_csv(file)

gsheet_id = ''
sheet_name = ''
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheet_id, sheet_name)
dff = pd.read_csv(gsheet_url)
try:
    for index, row in dff.iterrows():
        # 3 columns; Names, usernames and twitter URLs
        domain = row['Name']
        twt = row['Username']
        link = row['URL']
        Keywords = row['Keywords']
        # We create a tweet list as follows:
        # Accessing targeted account's timelines using their usernames(getting access to 200 recent tweets)
        tweets = api.user_timeline(screen_name=twt, count=200)
        # We store their tweets in a DataFrame and then filter them out later on based on the keywords we specify
        # We can also access when(time and date) each tweet were published
        data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        data['ID'] = np.array([tweet.id for tweet in tweets])
        data['Date'] = np.array([tweet.created_at for tweet in tweets])
        data['text'] = np.array([tweet.text for tweet in tweets])
        # At the moment we are only interested in officially published tweets rather than retweets
        # we can differentiate those two(tweets and retweets) using the bitwise operator shown below
        data = data[~data["Tweets"].str.contains("@")]

        # Avoid the same message from being sent on slack multiple times
        created_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=5)
        try:
            # Below are the keywords the sales department were interested in filtering tweets
            #keywords = ['Transport', 'velo', 'mobility', 'cycling', 'mobilité']
            dff.dropna(subset=['Keywords'], inplace=True)
            ndata = data[data['Tweets'].str.contains("|".join([keywords for keywords in dff['Keywords']]), regex=True, flags=re.IGNORECASE)].reset_index(drop=True)
            try:
                # check if there's a tweet stored in 'Tweets' columns
                if len(ndata['Tweets']) > 0:
                    for i in range(len(ndata['Tweets'])):
                        # If there's a tweet published, verify==True else it's False.
                        # It's True if both conditions are True; i.e True & True = True
                        verify = (data['Date'][i].tz_localize(None) > created_time) & (data['Date'][i].tz_localize(None) < datetime.datetime.utcnow())
                        if (verify == True):
                            # If the above condition is True, a message will be sent to 'filtered-tweets' - a Slack channel
                            SLACK_API.chat_postMessage(text=domain + ' tweeted :-  ' + ndata['Tweets'][i] + ' ' + link, channel='filtered-tweets')
                            #print('----', domain + ' tweeted :-  ' + ndata['Tweets'][i] + ' ' + link)
                        else:
                            pass
                else:
                    pass
            except Exception as e:
                pass
        except Exception:
            pass
# NB : For private Twitter accounts, it's not possible to see their tweets due to their privacy issue
# Making sure they don't throw errors if there are some in the targeted list using error handling method
except Exception:
    pass
print('___...___')






