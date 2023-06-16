import asyncio
import json
from web3 import Web3
from colorama import Fore
from websockets import connect

INFURA = "https://mainnet.infura.io/v3/0a762e0fa3d028c3aa513031"
INFURA_WS = "wss://mainnet.infura.io/ws/v3/0aa513031"
web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'{Fore.YELLOW} Connected: {Fore.WHITE} {web3.is_connected()}')

# ===============================================================================
def EventHandler(pending_tx):
    transaction = json.loads(pending_tx)
    txHash = transaction['params']['result']
    tx = web3.eth.get_transaction(txHash)
    if tx['to'] == web3.toChecksumAddress("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"):
        print(web3.toHex(tx['hash']))
    

async def subscribePendingTx():
    async with connect(INFURA_WS) as ws:
        await ws.send('{"jsonrpc": "2.0", "id": 1, "method": "eth_subscribe", "params": ["newPendingTransactions"]}')

        while True:
            try:
                pending_tx = await asyncio.wait_for(ws.recv(), timeout=15)
                EventHandler(pending_tx)
            except KeyboardInterrupt:
                exit()
            except:
                pass

if __name__ == "__main__":
    while True:
        asyncio.run(subscribePendingTx())


# swapExactTokensForTokensSupportingFeeOnTransferTokens()
# swapExactETHForTokensSupportingFeeOnTransferTokens()
# swapExactTokensForETHSupportingFeeOnTransferTokens()
# Filtering uniswap router all pending hash
# Filtering uniswap new create pair

#uniswap factory
# tx['to'] == web3.toChecksumAddress("0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f")
# tx['to'] == web3.toChecksumAddress("0x1F98431c8aD98523631AE4a59f267346ea31F984"):
      
