import tweepy
import pandas as pd

#tweepyをインポート　
CONSUMER_KEY = '8qqYKpCmhHz12maFnAZtH1Tiq'
CONSUMER_SECRET = 'OVsabb6XA6wXSBwcBrgjb5ZkZbRDkgoEfo3qRHlNygbDrFoPGk'
ACCESS_TOKEN = '1430529673-8DKgzTYLxQJSsNl3R4cr7ojFagvGHXgWG4K3oEw'
ACCESS_SECRET = 'Y1twCN883RURgdR1BZmRbMEvbHmlZ851eO42BAzvWNCaE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

screen_name = "tyksgk"

def extract_twitter_data(screen_name):
    twitterData = api.get_user(screen_name)
    account_information = pd.DataFrame({screen_name : [ twitterData.followers_count ,  str(twitterData.friends_count) , str(twitterData.statuses_count)]})
    account_information = account_information.T
    account_information.columns = ['フォロワー数' , 'フォロー数' , '投稿数']
    
    print(account_information)
extract_twitter_data(screen_name)
