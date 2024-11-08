import requests

response = requests.get("https://api.raydium.io/v2/main/pairs")
data = response.json()
print(data)

print(response.status_code)

print(data[0]['ammId'])
