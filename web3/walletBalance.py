owner = web3.toChecksumAddress("0x0DF6b519cbCDb5E411A56846540f6A56c")
balance_wei = web3.eth.getBalance(owner)
balance_ether = web3.fromWei(balance_wei, 'ether')
print('Balance ether: ', balance_ether)
