file = open('myFile.txt', 'w')

name = ['eth', 'bnb', 'sol', 'matic']
price = [100, 90, 80, 70]

for i in range(0, 4):
    if price[i] > 75:
        save_data = name[i] + " - " + str(price[i]) + "\n"
        file.write(save_data)
