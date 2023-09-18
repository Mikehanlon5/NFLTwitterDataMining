import tweepy
import pandas as pd

# set up Twitter API credentials
consumer_key = 'oLfZuj95jDLYBvve2dfAxQhN1'
consumer_secret = 'wvROkpIAu0qxc3MI9ndt4K8cfR21Dqj2KoAvnNMtnZ9W0HhHy3'
access_token = '1496924489946386439-ShhBFsCstq7XwbKn8LRPDdH9Yll5Ij'
access_token_secret = '6jXn91Dr6z0sPfVJcikS3QvUA0DDeTiH45eu335yWJMrm'
usernames = []
twts = []

# authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# define search query
search_words = "New England Patriots"
date_since = "2022-01-01"

# perform the search
tweets = tweepy.Cursor(api.search_tweets,
              q=search_words,
              lang="en",
              since_id=date_since).items(2500)

for tweet in tweets:
    usernames.append(tweet.user.screen_name)
    twts.append(tweet.text)

#adjust search term    
search_words = "New England Patriots"

tweets = tweepy.Cursor(api.search_tweets,
              q=search_words,
              lang="en",
              since_id=date_since).items(2500)

for tweet in tweets:
    usernames.append(tweet.user.screen_name)
    twts.append(tweet.text)

# Add mined tweets into dataset
data = {
    "username": usernames,
    "tweets": twts
}

print(len(twts))
print(len(usernames))

df = pd.DataFrame(data)
df.to_csv('PatriotsData.csv')