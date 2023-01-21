crypto = {
    'name': 'ETH',
    'price': 1500,
    'buy': True
}
crypto['2023'] = 'Good'
del crypto['2023']

print(crypto)
print(len(crypto))
print(crypto.keys())
print(crypto.values())
print(crypto.items())
print(crypto['price'])
