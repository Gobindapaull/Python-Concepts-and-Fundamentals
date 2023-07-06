from web3 import Web3
import os
from dotenv import load_dotenv
load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv('HTTP_URL')))
ws3 = Web3(Web3.WebsocketProvider(os.getenv('WEBSOCKET_URL')))

print('HTTPProvider: ', w3.is_connected())
print('WebsocketProvider: ', ws3.is_connected())
