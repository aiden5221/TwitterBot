import os
import time
import tweepy as tp

consumer_key = ' '
consumer_Secret = ''
access_Token = ''
token_Secret = ''

auth = tp.OAuthHandler(consumer_key, consumer_Secret)
auth.set_access_token(access_Token,token_Secret)
api = tp.API(auth)

os.chdir('pictures')
for kanye_image in os.listdir('.'):
    api.update_with_media(kanye_image)
    time.sleep(60)
