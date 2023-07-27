
import json
import requests
# 0xdac17f958d2ee523a2206206994597c13d831ec7
def get_token_price(token_address):
    try:
        response = requests.get(
            f'https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses={token_address}&vs_currencies=usd')
        data = response.json()
        print(data[token_address.lower()]['usd'])
    except Exception as e:
        print(f"Error fetching token price: {e}")

get_token_price('0xdac17f958d2ee523a2206206994597c13d831ec7')
