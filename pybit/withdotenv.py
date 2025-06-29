from pybit.unified_trading import HTTP
from dotenv import load_dotenv
import os
load_dotenv()


apikey=os.getenv("API_KEY")
secretkey=os.getenv("SECRET_KEY")

session = HTTP(
    testnet=True, # real account
    api_key=apikey,
    api_secret=secretkey
)

try:
    balance = session.get_wallet_balance(accountType="UNIFIED")
    wallet_balance = balance["result"]["list"][0]["totalWalletBalance"]
    print(balance)
    print(f"💰 Total Account Balance : {wallet_balance} USDT")
except Exception as e:
    print("Error Fetching balance: ", e)


# Great! ✅ This means your API keys are working perfectly, and you’ve successfully connected to the Bybit Unified Testnet account.
