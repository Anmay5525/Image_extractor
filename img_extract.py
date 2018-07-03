
import tweepy
import wget


consumerKey = "Your key here"
consumerSecret = "Your key here"
accessToken = "Your key here"
accessTokenSecret = "Your key here"

auth = tweepy.OAuthHandler(consumer_key = consumerKey, consumer_secret = consumerSecret)
auth.set_access_token(accessToken , accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter the hashtag to search for ")
n = int(input("Enter the number of tweets to search for "))

tweets = tweepy.Cursor(api.search, q = searchTerm, result_type = "recent").items(n)

neg = 0
pos = 0
neu = 0
pol = 0

media_url = []

for tweet in tweets:

    media = tweet.entities.get('media',[])
    if(len(media)):
        media_url.append(media[0]['media_url'])

i = 1

for media in media_url:
    wget.download(media, out = str(i) + ".jpg")
    i+=1
