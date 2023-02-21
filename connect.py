from web3 import Web3

bsc = 'https://bsc-dataseed.binance.org/'
web3 = Web3(Web3.HTTPProvider(bsc))

print('connected to blockchain: ', web3.isConnected())
