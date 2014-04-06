options = {'ships':[5,4,3,3,2]}

def PrintOptions():
    print("\n")
    print("The Current settings are\n")
    print("1) Board Size: 10 x 10")
    print("2) Ships:", options['ships'],"\n")

def ChangeOptions(curoptions):
    choice = int(input("Which would you like to change? "))
    if choice == 2:
        print("Enter ship lengths separated by spaces.")
        ships = input().split()
        curoptions['ships'] = [int(ship) for ship in ships]

    return(curoptions)
