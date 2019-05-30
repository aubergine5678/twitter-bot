import tweepy
import os

consumer_key = 'Consumer key'
consumer_secret = 'Consumer secret key'
access_token = 'Access toekn'
access_token_secret = 'Access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()

os.system('clear')
print("Currently logged it as:")
print (user.name)
print("-------------------------")
print("What do you want to do?")
print("1. - Send a tweet")
print("2. - Follow back all your followers")
print("3. - Favourite tweets that contain a phrase")
print("E - Exit")
opt = input('>>> ')
if opt in ["1", "1."]:
    print("Enter tweet text:")
    message = input('>>> ')
    print("Sending tweet...")
    api.update_status(message)
    print("Tweet sent.")
    exit()
elif opt in ["2", "2."]:
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        print ("Followed everyone that is following " + user.name)
    exit()
elif opt in ["3", "3."]:
    print("Search term:")
    search = input('>>> ')
    print("Number of tweets to interact with:")
    numberOfTweets = input('>>> ')
    try:
        int(numberOfTweets)
    except ValueError:
        print("The input must be a number")
        exit()
    limit = int(numberOfTweets)
    for tweet in tweepy.Cursor(api.search, search).items(limit):
        try:
            tweet.favorite()
            print('Favourited the tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    exit()
elif opt in ["e", "E", "exit", "q", "Q", "quit"]:
    exit()
else:
    print("That is not a valid option")
