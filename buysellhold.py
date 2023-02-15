import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from binance.um_futures import UMFutures
from config import api_key, secret_key

client = UMFutures(api_key, secret_key)
symbol = 'BTCUSDT'
timeframe = '1d'
quantity = 3

klines = client.klines(symbol, timeframe)
df = pd.DataFrame(klines).iloc[:, :6]
df.columns = ['Time', 'open', 'high', 'low', 'close', 'Volume'] #Name of the columns
df['Time'] = pd.to_datetime(df['Time'], unit = 'ms') #convert ms to date
df.set_index('Time', inplace=True) #remove index

fast_ma = df['close'].rolling(window=50).mean()
slow_ma = df['close'].rolling(window=200).mean()

def trend_following_strategy(df, fast_ma, slow_ma):
    signal = []
    for i in range(len(df)):
        if fast_ma[i] > slow_ma[i]:
            signal.append(1) #buy signal
        elif fast_ma[i] < slow_ma[i]:
            signal.append(-1) #sell signal
        else:
            signal.append(0) #hold signal
    return signal

signals = trend_following_strategy(df, fast_ma, slow_ma)
df['signal'] = signals
print(df)

def open_order(symbol, side, quantity):
    order = client.new_order(
        symbol=symbol,
        side=side,
        type='MARKET',
        quantity=quantity
    )
    print('order opened', order)

in_position = False

if df['signal'].iloc[-1] == 1 and in_position == False:
    open_order(symbol, 'BUY', quantity=quantity)
    in_position = True

elif df['signal'].iloc[-1] == -1 and in_position == True:
    open_order(symbol, 'SELL', quantity=quantity)
    in_position = True
    
else:
    pass
    
