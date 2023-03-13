from web3 import Web3
eth = "https://mainnet.infura.io/v3/"
web3 = Web3(Web3.HTTPProvider(eth))
print('connected: ', web3.isConnected())

# block number
block = web3.eth.get_block('latest')
print('block number: ', block['number'])

# total tx in a block
tx_count = web3.eth.get_block_transaction_count(block['number'])
print('total tx count: ', tx_count)

# tx hash
for tx in block['transactions']:
    print('tx: ', web3.toHex(tx))

# approve tx hash
for approve in block['transactions']:
    value = web3.eth.get_transaction(web3.toHex(approve))
    if '095ea7b3' in value['input']:
        print('approve tx hash: ', web3.toHex(value['hash']))

#tx details
txhash = 
tx_details = web3.eth.get_transaction(txhash)
print('transaction details: ', tx_details)
print('chain Id: ', tx_details['chainId'])
print('gas Price: ', tx_details['gasPrice'])
print('eth sent: ', tx_details['value']/1e18)



