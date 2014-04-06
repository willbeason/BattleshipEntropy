import random
from Matrix import *

def Sdx(dx,ships):
    slist = []
    for i in range(1,dx+1):
        sum = 0
        for j in ships:
            sum += max(min(j,i,dx+1-i,dx+1-j),0)
        slist.append(sum)
    return(slist)

def Spos(dx,ship):
    return([[0+(j-i>=5) for i in range(j)] for j in range(11)])
        

def RowOps(row,numlist):
    ops = [0]*10
    dx = 0
    for i in range(10):
        if row[i] == '-': dx += 1
        else:
            for j in range(1,dx+1):
                ops[i-j] = numlist[dx-1][j-1]
            dx = 0
    for j in range(1,dx+1):
        ops[i-j+1] = numlist[dx-1][j-1]

    return(ops)



def CalcOps(grid,numlist):
    gridT = Transpose(grid)
    x_ops = []
    y_ops = []
    for cur_row in grid:
        x_ops.append(RowOps(cur_row,numlist))
    for cur_row in gridT:
        y_ops.append(RowOps(cur_row,numlist))
    y_ops = Transpose(y_ops)
    
    ops = [[x_ops[j][i]+y_ops[j][i] for i in range(10)] for j in range(10)]
    return(ops)
    

def GetPos(grid,numlist):
    gridT = Transpose(grid)
    x_ops = []
    y_ops = []
    for cur_row in grid:
        x_ops.append(RowOps(cur_row,numlist))
    for cur_row in gridT:
        y_ops.append(RowOps(cur_row,numlist))
    y_ops = Transpose(y_ops)
    
    return(xpos,ypos)

def PrintBoard(opsgrid):
    for row in opsgrid: print(row)
    print('\n\n')
    
def PrintBoard2(grid):
    for row in grid: print(' '.join(row))
    print('\n\n')
    

def Shoot(move,grid):
    x = move % 10
    y = int(move / 10)
    grid[y][x] = 'm'

def ChooseMove(opsgrid):
    flatops = Flatten(opsgrid)
    curmax = max(flatops)
    maxcount = flatops.count(curmax)
    maxs = [flatops.index(curmax)]
    for i in range(maxcount-1):
        maxs.append(flatops.index(curmax,maxs[i]+1))
    #print(curmax, maxs)
    newmove = random.choice(maxs)
    print(newmove)
    return(newmove)
