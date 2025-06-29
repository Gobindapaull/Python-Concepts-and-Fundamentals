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
    order = session.place_order(
        category="spot",
        symbol="SOLUSDT",
        side="SELL",
        orderType="Market",
        qty=0.1 # solana
    )
    print(order)
except Exception as e:
    print("Error Fetching balance: ", e)

