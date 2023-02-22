import tweepy
import requests
import json 
import time
import config

auth_handler = tweepy.OAuthHandler(consumer_key=config.API_KEY,consumer_secret=config.API_SECRET)
auth_handler.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)

api = tweepy.API(auth_handler, wait_on_rate_limit=True)

print('Logged in ')

while True:
    bitcoinprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    price = bitcoinprice.json()
    btcusd = price['bitcoin']['usd']
    print(btcusd)

    message = 'The current BTC Price is : ' + str(btcusd) + 'USD, Buy #Bitcoin now'
    api.update_status(message)
    print('Tweet was posted successfully')
    time.sleep(300)

