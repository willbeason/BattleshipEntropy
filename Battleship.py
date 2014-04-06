import random
import string
from Matrix import *
from GreedyAI import *
from Display import *
from Options import *

def GetPos(grid,numlist):
    gridT = Transpose(grid)
    x_ops = []
    y_ops = []
    for cur_row in grid:
        x_ops.append(RowOps(cur_row,numlist))
    xtot = sum(Flatten(x_ops))
    for cur_row in gridT:
        y_ops.append(RowOps(cur_row,numlist))
    y_ops = Transpose(y_ops)
    ytot = sum(Flatten(y_ops))

    all_ops = Flatten(Flatten([x_ops,y_ops]))
    posscore = random.randint(0,xtot+ytot)
    
    position = -1
    possum = 0
    while possum<posscore:
        position += 1
        possum += all_ops[position]

    xpos = int(position % 10)
    ypos = int(position % 100 / 10)
    horizontal = possum<xtot
    
    return(xpos,ypos,horizontal)

def PositionShips(grid,ships):
    for ship in ships:
        shipSD = [[0+(j-i>=ship) for i in range(j)] for j in range(1,11)]
        shipcenter = GetPos(grid,shipSD)
        if shipcenter[2]:
            for i in range(ship): grid[shipcenter[1]][shipcenter[0]-i] = ship
        else:
            for i in range(ship): grid[shipcenter[1]-i][shipcenter[0]] = ship

def mainmenu():
    menuops = open('menuoptions.txt','r').read()
    print(menuops)
    option = -1
    while option not in range(5):
        option = int(input("What would you like to do? "))
    return(option)


curgrid = FreshGrid()
shipposgrid = FreshGrid()

def main():
    mainchoice = 0
    
    print(open('intro.txt','r').read())

    while mainchoice != 4:
        mainchoice = mainmenu()

        if mainchoice == 1:
            PrintOptions()
            ChangeOptions(options)

        if mainchoice == 2:
            shipposgrid = FreshGrid()
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
