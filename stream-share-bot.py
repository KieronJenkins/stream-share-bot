import tweepy
import time

#Keys have been taken out of code
consumer_key = "------"
consumer_secret = "------"
access_token = "------"
access_token_secret = "------"
#Authentication Keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #Auth Keys
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)

#Start of Bot
user = api.me()
search = "#smallstreamer" or "#supportsmallstreamers" #Hashtags to be searched for
retweet_hashtag = "#streamsharebot"
tweet_limit = int(250) #Limit on how many tweets the bot will do

#Start of code for liking tweets
def twitter_like():
    for t in tweepy.Cursor(api.search, search).items(tweet_limit): #Searching for hashtags
        try:
            print("Liked Tweet")
            t.favorite() #Like a tweet with hashtag
            time.sleep(60) #Wait for 60 seconds
            twitter_retweet() #Move to retweet function
        except tweepy.TweepError as error:
            print(error.reason)
        except StopIteration:
            break


def twitter_retweet():
    for rt in tweepy.Cursor(api.search, retweet_hashtag).items(tweet_limit):
        try:
            print("Retweeted Tweet")
            rt.retweet()
            time.sleep(60)
            twitter_like()
        except tweepy.TweepError as error:
            print(error.reason)
        except StopIteration:
            break

twitter_like()
