
from web3 import Web3

# connect to block chain
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
print("Connected to binance blockchain network : " , web3.is_connected())

# nonce of an address
sender_address = web3.to_checksum_address("0xdbd9730fA39880e8266Ed3B382adE15BC9A5FE28")
nonce = web3.eth.get_transaction_count(sender_address)
print('nounce: ', nonce)
