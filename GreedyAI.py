import random

readboard = open('startboard.txt','r')
curgrid = readboard.read().split()
for i in range(len(curgrid)):
    curgrid[i] = list(curgrid[i])


ships = [2,3,3,4,5]

def Transpose(array):
    array = [[array[i][j] for i in range(len(array))] for j in range(len(array[0]))]
    return(array)

def Flatten(array):
    array = [item for sublist in array for item in sublist]
    return(array)

def Sdx(dx):
    slist = []
    for i in range(1,dx+1):
        sum = 0
        for j in ships:
            sum += max(min(j,i,dx+1-i,dx+1-j),0)
        slist.append(sum)
    return(slist)

def RowOps(row):
    ops = [0]*10
    dx = 0
    for i in range(10):
        if row[i] == '-': dx += 1
        else:
            for j in range(1,dx+1):
                ops[i-j] = eSd[dx-1][j-1]
            dx = 0
    for j in range(1,dx+1):
        ops[i-j+1] = eSd[dx-1][j-1]

    return(ops)

def CalcOps(grid):
    gridT = Transpose(grid)
    x_ops = []
    y_ops = []
    for cur_row in grid:
        x_ops.append(RowOps(cur_row))
    for cur_row in gridT:
        y_ops.append(RowOps(cur_row))
    y_ops = Transpose(y_ops)
    
    ops = [[x_ops[i][j]+y_ops[i][j] for i in range(10)] for j in range(10)]
    return(ops)
    

def PrintBoard(opsgrid):
    for row in opsgrid: print(row)
    print('\n\n')
    

def Shoot(move,grid):
    x = move % 10
    y = int(move / 10)
    grid[x][y] = 'm'

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
    

eSd = []
for i in range(1,11): eSd.append(Sdx(i))

newops = CalcOps(curgrid)
PrintBoard(newops)


for i in range(3):
   nextmove = ChooseMove(newops)
   Shoot(nextmove,curgrid)
   newops = CalcOps(curgrid)
   #PrintBoard(newops)

PrintBoard(curgrid)
PrintBoard(newops)
print(sum(Flatten(newops)))

#print('\n\n')
#curgrid[4][4] = 'm'
#newops = CalcOps(curgrid)
#for row in newops: print(row)



