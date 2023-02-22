import requests
import json

bitcoinprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').json()


print(bitcoinprice)
