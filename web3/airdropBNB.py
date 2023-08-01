from web3 import Web3
import config
import time

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
print('connected : ', web3.is_connected())

sender = "0x09ec269360504cA3A0E475dCAe7822B2a778A97b"
receiver = ['0x422B0755EABeA90Cc2C5674F8Bba65C861962fdD','0x5BAa2Ff2696258ad36727dE8254B7d505600d333','0x0DF6b519cbCDb49efBC45E411A56846540f6A56c','0x4d4721B12B4C45205E1F8A1A7fDAf700C3140DAD']

bal = web3.eth.get_balance(sender)
balance = web3.from_wei(bal, 'ether')
print('sender bnb balance: ', balance)

for i in receiver:
    print('receiver address: ', i)

    tx = {
        'nonce': web3.eth.get_transaction_count(sender),
        'to': web3.to_checksum_address(i),
        'value': web3.to_wei(0.00000001, 'ether'),
        'gas': 21000,
        'gasPrice': web3.to_wei(50, 'gwei')
    }

    signed_tx = web3.eth.account.sign_transaction(tx, config.private)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    transaction = web3.to_hex(tx_hash)
    print('transaction : ', transaction)
    time.sleep(10)
