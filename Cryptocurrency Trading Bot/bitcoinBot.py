import pandas as pd
from binance.client import Client
import numpy as np

client = Client()

def getdata(symbol, start):
    frame = pd.DataFrame(client.get_historical_klines(
        symbol,
        '1h',
        start
    ))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame.set_index('Time', inplace=True)
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    return frame

df = getdata('BTCUSDT', '2023-01-01')
df['chg'] = np.log(df.Close.pct_change() + 1)
df['12h_chg'] = df.chg.rolling(12).sum()
df.dropna(inplace=True)
df['buyprice'] = df.Open.shift(-1)

def profitcalc(change, tp, sl):
    in_position = False
    profits = []

    for index, row in df.iterrows():
        if not in_position:
            if row['12h_chg'] > change:
                buyprice = row.buyprice
                in_position = True
        
        if in_position:
            if row.High >= buyprice * tp:
                sellprice = buyprice * tp # 1% increase
                profit = (sellprice - buyprice) / buyprice
                profits.append(profit)
                in_position = False

        elif row.Low <= buyprice * sl:

            sellprice = buyprice * sl
            profit = (sellprice - buyprice) / buyprice
            profits.append(profit)
            in_position = False

    return (pd.Series(profits) + 1).prod() - 1

profitcalc(0.02, 1.04, 0.96)
arr = np.arrange(0.01, 0.16, 0.01)

for ele in arr:
    print('for' + str(ele))
    print(profitcalc(0.02, 1 + ele, 1 - ele))


