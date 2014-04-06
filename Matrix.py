def Transpose(array):
    array = [[array[i][j] for i in range(len(array))] for j in range(len(array[0]))]
    return(array)

def Flatten(array):
    array = [item for sublist in array for item in sublist]
    return(array)

def UnFlatten(array,n=10):
    array = [[array[j*10+i]  for i in range(n) ] for j in range(n) ]
    return(array)

def FreshGrid():
    return(UnFlatten(open('startboard.txt','r').read().split()))
