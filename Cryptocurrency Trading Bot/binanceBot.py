import pandas as pd
import ta
from binance import Client
from datetime import timedelta
import time
import requests

client = Client("",
                "")

symbol = 'ETHUSDT'

def getdata(symbol):
    frame = pd.DataFrame(client.get_historical_klines(symbol, '15m', '3000 minutes UTC'))
    frame = frame.iloc[:,0:5]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close']
    frame.set_index('Time', inplace=True)
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    return frame

df = getdata()

def indicators(df):
    df['SMA_200'] = ta.trend.sma_indicator(df.Close, window=200)
    df['stochrsi_k'] = ta.momentum.stochrsi_k(df.Close, window=10)
    df.dropna(inplace=True)
    df['Buy'] = (df.Close > df.SMA_200) & (df.stochrsi_k < 0.05)
    return df

indicators(df)

def pricecalc(symbol, limit=0.97):
    raw_price = float(client.get_symbol_ticker(symbol=symbol)['price'])
    dec_len = len(str(raw_price).split('.')[1])
    price = raw_price * limit
    return round(price, dec_len)

def quantitycalc(symbol, investment):
    info = client.get_symbol_info(symbol=symbol)
    Lotsize = float([i for i in info['filters'] if
                     i['filterType'] == 'LOT_SIZE'][0]['minQty'])
    price = pricecalc(symbol)
    qty = round(investment/price, right_rounding(Lotsize))
    return qty

def right_rounding(Lotsize):
    splitted = str(Lotsize).split('.')
    if float(splitted[0]) == 1:
        return 0
    else:
        return len(splitted[1])

def buy(investment):
    order = client.order_limit_buy(symbol=symbol,
                                   price= pricecalc(symbol),
                                   quantity= quantitycalc(symbol, investment))
    print(order)
    pos_dict['in_position'] = True
    return order

def sell(qty):
    order = client.create_order(symbol=symbol,
                                side="SELL",
                                type="MARKET",
                                quantity=qty
                            )
    print(order)
    pos_dict['in_position'] = False

pos_dict = {'in_position': False}

def checkbuy(investment):
    if not pos_dict['in_position']:
        if df.Buy.values:
            return True
    else:
        print("already in a position")

def checksell(order):
    order_status = client.get_order(symbol=symbol,
                                    orderId=order['orderId']
                                    )
    if pos_dict['in_position']:
        if order_status['status'] == 'NEW':
            print("buy limit order is pending")
        elif order_status['status'] == 'FILLED':
            cond1 = df.Close.values > float(order_status['price'])
            cond2 = pd.to_datetime('now') >= pd.to_datetime(
                order_status['updateTime'], unit='ms'
            ) + timedelta(minutes=150)
            if cond1 or cond2:
                sell(order_status['origQty'])
    else:
        print('currently not in position, no checks for selling')

investment = 100

while True:
    df = indicators(getdata(symbol))
    if checkbuy(investment):
        current_order = buy(investment)
    try:
        checksell(current_order)
    except:
        print('Not an order yet')
    time.sleep(10 * 60)


