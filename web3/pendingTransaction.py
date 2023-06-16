import asyncio
import json
from web3 import Web3
from colorama import Fore
from websockets import connect

INFURA = "https://mainnet.infura.io/v3/0a762e0fac61466ca3ddfdfc3aa513031"
INFURA_WS = "wss://mainnet.infura.io/ws/v3/0a762e0fac61dfdfda3d028c3aa513031"
web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'{Fore.YELLOW} Connected: {Fore.WHITE} {web3.is_connected()}')

# ===============================================================================
def EventHandler(pending_tx):
    transaction = json.loads(pending_tx)
    txHash = transaction['params']['result']
    print(txHash)
    #print(web3.eth.get_transaction(txHash))


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
