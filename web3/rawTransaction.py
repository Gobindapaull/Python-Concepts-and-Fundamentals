from web3 import Web3
import config
url = "https://mainnet.infura.io/v3/"
web3 = Web3(Web3.HTTPProvider(url))
print("Connected: ", web3.isConnected())

balance = web3.eth.get_balance("")
print("balance: ", balance)

from_account = ""
to_account = ""

address_1 = web3.toChecksumAddress(from_account)
address_2 = web3.toChecksumAddress(to_account)

nonce = web3.eth.getTransactionCount(address_1)

tx = {
    'nonce': nonce,
    'to': address_2,
    'value': web3.toWei(0.0001, 'ether'),
    'gas': 21000,
    'gasPrice': web3.toWei(40, 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, config.private_key)
tx_transaction = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(tx_transaction)

