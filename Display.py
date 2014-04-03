import string

def PrintBoard(grid,lines=2):
    rowtext = '    '
    for n in range(10): rowtext += ' %1s ' %n
    print(rowtext)
    
    i = 0
    for row in grid:
        rowtext = '%2d0|' %i
        for item in row: rowtext += '%3d' %item
        print(rowtext)
        i += 1
        
    print('\n'*lines)
    
def PrintBoard2(grid,lines=2):
    rowtext = '    '
    for n in range(10): rowtext += ' %1s ' %n
    print(rowtext)
    
    i = 0
    for row in grid:
        rowtext = '%2d0| ' %i
        for item in row: rowtext += ' %s ' %item
        print(rowtext)
        i += 1
    print('\n'*lines)
