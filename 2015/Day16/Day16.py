
# %% Imports
import re

# %% Load Data
with open('Day16.input', 'r') as f:
    data = f.read().splitlines()
    
        
# %%
# Parse
sues = {}
for line in data:
    sueno = line.split(': ',maxsplit=1)[0].split(' ')[1]
    sueno = int(sueno)
    params = line.split(': ', maxsplit=1)[1].split(',')
    sues[sueno] = {f.split(': ')[0].strip(): int(f.split(': ')[1]) for f in params}
        
    
# %%
# Wanted Info from puzzle
wanted = {'children': 3,\
'cats': 7,\
'samoyeds': 2,\
'pomeranians': 3,\
'akitas': 0,\
'vizslas': 0,\
'goldfish': 5,\
'trees': 3,\
'cars': 2,\
'perfumes': 1}
    
def checkParam(param, value):
    if wanted[param] == value:
        return True
    else:
        return False

def checkSue(num):
    for i in sues[num]:
        if checkParam(i, sues[num][i]):
            continue
        else:
            return False
    return True

good = []
for idx in range(1,501):
    if checkSue(idx):
        good.append(idx)
        
print('The answer to part 1 is: {}'.format(good))

# %%
# Part 2
def checkParam2(param, value):
    """ Cats and trees readings are greater than
    pomeranians and goldfish are less than"""
    if param in ['cats', 'trees']:
        if wanted[param] < value:
            return True
        else:
            return False
    elif param in ['pomeranians', 'goldfish']:
        if wanted[param] > value:
            return True
        else:
            return False
    else:
        if wanted[param] == value:
            return True
        else:
            return False
            
def checkSue2(num):
    for i in sues[num]:
        if checkParam2(i, sues[num][i]):
            continue
        else:
            return False
    return True
            
good = []
for idx in range(1,501):
    if checkSue2(idx):
        good.append(idx)
        
print('The answer to part 2 is: {}'.format(good))          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            