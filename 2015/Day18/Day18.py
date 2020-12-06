debug = False

import numpy as np

if debug:
    with open('Day18.example', 'r') as f:
        data = f.read().splitlines()
    steps = 5
else:
    with open('Day18.input', 'r') as f:
        data = f.read().splitlines()  
    steps = 100
       
""" # - on
    . - off
    8 neighbors (include diagonals)
    if on edge, missing neighbors count as OFF
    
    Light that is ON stays ON if 2 or 3 neighbors are ON, OFF otherwise
    Light that is OFF turns ON only if 3 neighbors are ON, OFF otherwise
"""

# currentGen = [[None]*len(data[0])]*len(data)
# for row in range(len(data)):
#     currentGen[row] = list(data[row])
currentGen = np.ones([len(data),len(data[0])],dtype='str')
for row in range(len(data)):
    for col in range(len(data[0])):
        currentGen[row,col] = data[row][col]
oldGen = []
    
# %%

# countOnNeighbors
def countOnNeighbors(row,col):
    count = 0
    # Previous Row
    if row-1 >= 0:
        if col -1 >= 0:
            # print('Row: {} Col: {}'.format(row-1, col-1))
            if currentGen[row-1, col-1] =='#':
                count += 1
        if col + 1 <= len(currentGen[0])-1:
            # print('Row: {} Col: {}'.format(row-1, col+1))
            if currentGen[row-1, col+1] == '#':
                count += 1
        if currentGen[row-1, col] == '#':
            # print('Row: {} Col: {}'.format(row-1, col))
            count += 1
    # Next Row
    if row + 1 <= len(currentGen)-1:
        if col - 1 >= 0:
            if currentGen[row+1, col-1] =='#':
                count += 1
        if col + 1 <= len(currentGen[0])-1:
            if currentGen[row+1, col+1] == '#':
                count += 1
        if currentGen[row+1, col] == '#':
            count += 1
    # This Row
    if col - 1 >= 0:
        if currentGen[row, col-1] =='#':
            count += 1
    if col + 1 <= len(currentGen[0])-1:
        if currentGen[row, col+1] == '#':
            count += 1
    return count

# Figure out next iter's state:
def nextStep(row,col):
    n = countOnNeighbors(row,col)
    if currentGen[row, col] == '#':  # If light currently on
        if n in [2,3]:
            nextGen = '#'
        else:
            nextGen = '.'
    else:  # If light currently off
        if n == 3:
            nextGen = '#'
        else:
            nextGen = '.'
    return nextGen

# Assemble next Generation's map
def calcNextGen():
    nextMap = np.ones([len(data),len(data[0])],dtype='str')
    for row in range(len(currentGen)):
        for col in range(len(currentGen[0])):
            nextMap[row, col] = nextStep(row, col)
    return nextMap

def count(inGen):
    count = 0
    for i in inGen:
        for j in i:
            if j == '#':
                count += 1
    return count

# %%
# Part 1 answer
# Save Old gen, load new
for i in range(steps):
    oldGen.append(data)
    currentGen = calcNextGen()

print('The anwser to part one is: {}'.format(count(currentGen)))
# It's not 2438

# %%
currentGen = np.ones([len(data),len(data[0])],dtype='str')
for row in range(len(data)):
    for col in range(len(data[0])):
        currentGen[row,col] = data[row][col]
oldGen = []

def fixCorners(inp):
    inp[0,0] = '#'
    maxRow, maxCol = inp.shape
    maxRow -= 1
    maxCol -= 1
    inp[0,maxCol] = '#'
    inp[maxRow,0] = '#'
    inp[maxRow, maxCol] = '#'
    return inp

for i in range(steps):
    currentGen = fixCorners(currentGen)
    # print('######## STEP {} #####'.format(i))
    # print(currentGen)
    oldGen.append(currentGen)
    currentGen = calcNextGen()
    currentGen = fixCorners(currentGen)
    
print('The answer to part two is {}'.format(count(currentGen)))
    
    
    
    
    
    
    
    
    
    
    
    
    