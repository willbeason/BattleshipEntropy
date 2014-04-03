def Transpose(array):
    array = [[array[i][j] for i in range(len(array))] for j in range(len(array[0]))]
    return(array)

def Flatten(array):
    array = [item for sublist in array for item in sublist]
    return(array)

