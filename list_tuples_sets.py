crypto = ['BNB', 'ETH', 'SOL', 'USDT', 'TRON', 'USDC', 'DAI']

crypto.append('New Coin')
crypto.insert(3, 'BTC')
crypto.remove('SOL')
crypto.pop()
crypto.reverse()

price = [300, 1000, 100, 1, 0.5, 1.1, 1.2]
price.sort()
print(price)
print(min(price))
print(max(price))
print(sum(price))

for i, name in enumerate(price, start=1):
    print(i, name)

print(crypto)
print(len(crypto))
print(crypto[0]) #first element
print(crypto[-1]) #last element

#Sets
crypto_sets = {'BNB', 'ETH', 'SOL', 'USDT', 'TRON', 'USDC', 'DAI', 'DAI'}
crypto1_sets = {'BNB', 'ETH', 'SOL'}

print(crypto_sets)
print(crypto_sets.intersection(crypto1_sets))
print(crypto_sets.difference(crypto1_sets))
print(crypto_sets.union(crypto1_sets))

#empty list
empty_list = []
print(empty_list)
print(type(empty_list))

#empty tuple
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

#empty_sets
empty_set = {}
print(empty_set)
print(type(empty_set))
