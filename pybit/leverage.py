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
    positions = session.get_positions(
        category="linear",
        symbol="BTCUSDT"
    )
    current_leverage = positions["result"]["list"][0]["leverage"]
    print(f"Current leverage: {current_leverage}x")
except Exception as e:
    print("Error Fetching balance: ", e)

