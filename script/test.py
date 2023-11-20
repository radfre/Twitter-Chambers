from Read import Read
import tweepy
from textblob import TextBlob
import networkx as nx
import matplotlib.pyplot as plt

read = Read('../Credential.txt')

# API keyws that yous saved earlier
consumer_key = read.cons_API_Key()
consumer_secret = read.cons_API_secret()
access_token = read.access_token()
access_token_secret = read.access_token_secret()

# Authenticate to Twitter
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)


user_id = 1726372280035311616.

# By default, only the ID, name, and username fields of each user will be
# returned
# Additional fields can be retrieved using the user_fields parameter
response = client.get_users_followers(
    user_id, user_fields=["profile_image_url"]
)

for user in response.data:
    print(user.username, user.profile_image_url)

# By default, this endpoint/method returns 100 results
# You can retrieve up to 1000 users by specifying max_results
response = client.get_users_followers(user_id, max_results=1000)
