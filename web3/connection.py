from web3 import Web3
from colorama import Fore

INFURA = "https://mainnet.infura.io/v3/0a762e0fac61466ca3d028cdfdf3aa513031"
web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'{Fore.YELLOW} Connected: {Fore.WHITE} {web3.is_connected()}')
