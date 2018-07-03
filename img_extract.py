
import tweepy
import wget


consumerKey = "49qN5k1Trnz060Bp1MdgzYD4s"
consumerSecret = "MtumQPNeToT7c3aGEtIsdfdw5J4ADR0C9c21irPYC3FoQNFms6"
accessToken = "1009111317024792576-Nz2evvUeDWi1ZQh9wm1HoCeXVsWCDG"
accessTokenSecret = "3BneR1cAlUgAOX54nU4J1g5E5ZU317QulsU3KWT0HHTzY"

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