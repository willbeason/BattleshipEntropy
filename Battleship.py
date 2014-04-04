import random
import string
from Matrix import *
from GreedyAI import *
from Display import *
from Options import *

def PositionShips(grid,ships):
    for ship in ships:
        print(ship)
        shipSD = [Sdx(i,[ship]) for i in range(1,11)]
        PrintBoard(CalcOps(grid,shipSD))

def mainmenu():
    menuops = open('menuoptions.txt','r').read()
    print(menuops)
    option = -1
    while option not in range(4):
        option = int(input("What would you like to do? "))
    return(option)

def main():
    mainchoice = 0
 
    shipposgrid = [['-']*10]*10
    curgrid = [['-']*10]*10
    
    print(open('intro.txt','r').read())

    while mainchoice != 4:
        mainchoice = mainmenu()

        if mainchoice == 1:
            PrintOptions()
            ChangeOptions(options)

        if mainchoice == 2:
            ships = options['ships']
            PositionShips(shipposgrid,ships)
            PrintBoard2(shipposgrid)
            
        if mainchoice == 3:
            ships = options['ships']
            
            for i in range(10):
                curgrid.append(griddata[i*10:i*10+10])
            
            eSd = [Sdx(i,ships) for i in range(1,11)]

            newops = CalcOps(curgrid,eSd)
            PrintBoard(newops)

            anothermove = True
            while anothermove:

                nextmove = ChooseMove(newops)
                Shoot(nextmove,curgrid)
                newops = CalcOps(curgrid,eSd)
                PrintBoard2(curgrid)
                anothermove = '' == input('Press enter to play a move.')

            PrintBoard2(curgrid)
            PrintBoard(newops)
            print(sum(Flatten(newops)))
    

if __name__ == "__main__":
    main()
