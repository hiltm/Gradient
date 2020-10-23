from twython import Twython
from instabot import Bot
from Keys import *

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

bot = Bot()
bot.login(username = "insta_username",
          password = "insta_password")

def tweet_image(filename):
    image = open(filename, 'rb')
    response = twitter.upload_media(media=image)
    media_id = [response['media_id']]
    twitter.update_status(media_ids=media_id)

def insta_image(filename):
    bot.upload_photo(filename)

