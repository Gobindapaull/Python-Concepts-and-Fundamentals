import config
import coinbasepro

public_client = coinbasepro.PublicClient()

client = coinbasepro.AuthenticationClient(
    config.api_key,
    config.api_secret,
    config.api_pass,
    api_url = config.cbpro_url
)

accounts = client.get_accounts()
total_price = 0

for account in accounts:
    #print(account)
    stock = account.get('currency')
    quantity = float(account.get('balance'))
    price = float(account.get('available'))

    if float((price) > 0):
        account_id = account.get('currency')
        if (account_id != 'USD'):
            stock_price = float(public_client.get_product_ticker(product_id = stock+'-USD').get(price))
            print('stock price', stock_price)
            total_price = (total_price + quantity * stock_price)

print(total_price)
