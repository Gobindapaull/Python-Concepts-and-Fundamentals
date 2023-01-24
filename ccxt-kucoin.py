import ccxt
import config

kucoin = ccxt.kucoin({
    'enableRateLimit': True,
    'apiKey': config.apiKey,
    'apiSecret': config.apiSecret
})

print(kucoin.fetch_balance())

#config.py
apiKey="abc"
apiSecret="cba"
