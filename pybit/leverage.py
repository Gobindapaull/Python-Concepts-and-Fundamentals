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

positions = session.get_positions(
        category="linear",
        symbol="BTCUSDT"
    )
current_leverage = positions["result"]["list"][0]["leverage"]
print(f"Current leverage: {current_leverage}x")

# Set to 10x leverage with error handling
try:
    session.set_leverage(
        category="linear",
        symbol="BTCUSDT",
        buyLeverage="10",
        sellLeverage="10"
    )
except Exception as e:
    print("Leverage setting failed: ", e)

# Place buy order
order = session.place_order(
    category="linear",
    symbol="BTCUSDT",
    side="Buy",
    orderType="Market",
    qty="0.0001",
    positionIdx=1
)
print(order)


