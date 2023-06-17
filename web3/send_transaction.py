from web3 import Web3

bsc_url = "https://bsc-dataseed.binance.org"
web3 = Web3(Web3.HTTPProvider(bsc_url))

print(web3.is_connected())

# ----------------------------------------------------------------- 

sender = ""
private_key = ""

receiver = ""

# ---------------------------------------------------------------------

nonce = web3.eth.get_transaction_count(sender)
tx = {
    'nonce': nonce,
    'to': receiver,
    'value': web3.to_wei(0.0001, 'ether'),
    'gas': 21000,
    'gasPrice': web3.to_wei('5', 'gwei')
}

# -----------------------------------------------------------------

signed_tx = web3.eth.account.sign_transaction(tx, private_key)
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

print(f'https://bscscan.com/tx/'+web3.to_hex(tx_hash))
# https://bscscan.com/tx/0x9755814f8799f7aebbf0e468b92f646dff224c8ace4d8f124f007d096315b597
