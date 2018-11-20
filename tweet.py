import tweepy
import pandas as pd

CONSUMER_KEY = '8qqYKpCmhHz12maFnAZtH1Tiq'
CONSUMER_SECRET = 'OVsabb6XA6wXSBwcBrgjb5ZkZbRDkgoEfo3qRHlNygbDrFoPGk'
ACCESS_TOKEN = '1430529673-8DKgzTYLxQJSsNl3R4cr7ojFagvGHXgWG4K3oEw'
ACCESS_SECRET = 'Y1twCN883RURgdR1BZmRbMEvbHmlZ851eO42BAzvWNCaE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

screen_name = "ryuu_yrrrr"

class Tweet:
    def __init__(self,screen_name):
        self.screen_name = screen_name

    def tweets_data(self,screen_name):
        tweet_data=[]
        for tweet in tweepy.Cursor(api.user_timeline,screen_name,exclude_replies = True).items():
            tweet_data.append([tweet.created_at,tweet.text.replace('/n',''),tweet.favorite_count,tweet.retweet_count])
        tweet_information = pd.DataFrame(tweet_data)
        tweet_information.columns = ['Time' , 'Tweet' , 'NumberofFavorite' , 'NumberofRetweet']
        tweet_information['RT']=0
        #RTしていたら'1'と表記する
        tweet_information.loc[tweet_information['Tweet'].str.startswith('RT')  ,'RT'] = 1
        print(tweet_information)

tweet = Tweet(screen_name)
tweet.tweets_data(screen_name)