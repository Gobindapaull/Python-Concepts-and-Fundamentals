def parent_function(person, coins):

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print(person + " has " + str(coins) + " coins left")
        elif coins == 1:
            print(person + " has " + str(coins) + " coins left")
        else:
            print(person + " is out of coins")
        
    return play_game

tommy = parent_function("Tommy", 10)
jimmy = parent_function("Jimmy", 5)

tommy()
tommy()
jimmy()
