# 1
countries = ["USA", "INDIA", "CANADA", "JAPAN"]
for country in countries:

    print(country)

# 2
word = "INDIA"
for letter in word:
    print(letter) # I, N, D, I, A

# 3
for i in range(1, 11):
    print(i) # 1 inclued and 11 excluded

# 4
j = 0
while (j <= 5):
    print(j) # 0, 1, 2, 3, 4, 5
    j += 1

# 5
for i in range(3, 29, 4):
    print(i) # 3, 7, 11, 15, 19, 23, 27

# 6
sum = 0
for number in range(1, 5):
    sum = sum + number

print("Sum: ", sum)

# 7
for i in range(1, 7):
    if ( i == 3 ): # skip 3
        continue
    print(i) # 7 excluded

# 8
for letter in "computer":
    if (letter == "t"):
        print('t found: ')
        break
    print(letter)
