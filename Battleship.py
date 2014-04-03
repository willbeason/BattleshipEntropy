import random
import string
from Matrix import *
from GreedyAI import *
from Display import *
from Options import *

def mainmenu():
    menuops = open('menuoptions.txt','r').read()
    print(menuops)
    option = -1
    while option not in range(4):
        option = int(input("What would you like to do? "))
    return(option)

def main():
    mainchoice = 0
    
    readboard = open('startboard.txt','r')
    griddata = readboard.read().split()
    curgrid = []
    

    
    introtext = open('intro.txt','r').read()
    print(introtext)

    while mainchoice != 3:
        mainchoice = mainmenu()

        if mainchoice == 1:
            PrintOptions()
            ChangeOptions(options)

        if mainchoice == 2:
            ships = options['ships']
            
            for i in range(10):
                curgrid.append(griddata[i*10:i*10+10])
            
            eSd = []
            for i in range(1,11): eSd.append(Sdx(i,ships))

            newops = CalcOps(curgrid,eSd)
            PrintBoard(newops)

            anothermove = True
            while anothermove:
                anothermove = 'Y' == input('Play another move? ')

                nextmove = ChooseMove(newops)
                Shoot(nextmove,curgrid)
                newops = CalcOps(curgrid,eSd)
                #PrintBoard(newops)

            PrintBoard2(curgrid)
            PrintBoard(newops)
            print(sum(Flatten(newops)))
    

if __name__ == "__main__":
    main()
