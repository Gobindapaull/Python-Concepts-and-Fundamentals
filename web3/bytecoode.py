# byte code of a contract

getCode = web3.eth.get_code("0x514910771AF9Ca656af840dff83E8264EcF986CA")
print('get code: ', web3.toHex(getCode))
