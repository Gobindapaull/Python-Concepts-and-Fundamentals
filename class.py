class Crypto():
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol
    def price_inc(self):
        self.price = int(self.price*1.15) # 15% increase price
    
BNB = Crypto(300, "BNB")
ETH = Crypto(1500, "ETH")

print(BNB.__dict__)

ETH.price_inc()
print(ETH.price)
