from web3 import Web3
import config

#connect to blockchain

web3 = Web3(Web3.HTTPProvider(config.INFURA))
print('Connected to Ethereum Blockchain: ', web3.isConnected())

#connect to smart contract

target_address = web3.toChecksumAddress("0x4A25F3815E159582E1E2E7805b78Db8e4cB12768")
target_ABI = '[{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_swingby","type":"address"},{"internalType":"uint256","name":"_apr","type":"uint256"},{"internalType":"address","name":"_source","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Claim","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"ackFunds","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"apr","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"balanceBefore","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"barn","outputs":[{"internalType":"contract IBarn","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claim","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"currentMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"emergencyWithdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"lastPullTs","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"owed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"registerUserAction","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"rewardToken","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_barn","type":"address"},{"internalType":"uint256","name":"_startTs","type":"uint256"}],"name":"setBarn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_apr","type":"uint256"}],"name":"setNewAPR","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"source","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"userMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
target = web3.eth.contract(address=target_address, abi=target_ABI)

apr = target.functions.apr().call() #read contract function
owner = target.functions.owner().call()
rewardToken = target.functions.rewardToken().call()

print('rewardToken: ', rewardToken)
print('owner: ', owner)
print('apr', apr) 
