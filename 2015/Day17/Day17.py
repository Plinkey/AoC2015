debug = False
import itertools
import numpy as np 

# %% Load Data
if debug:
    data = [20, 15, 10, 5, 5]
    goal = 25
else:
    with open('Day17.input', 'r') as f:
        data = f.read().splitlines()
    goal = 150
    
jars = [int(i) for i in data]



# %%
# PART ONE       
combos = []
for L in range(1, len(jars)+1):
    for subset in itertools.combinations(jars, L):
        combos.append(subset)
        
count = 0
for c in combos:
    if np.sum(c) == goal:
        count += 1
        
print('The answer to part one is: {}'.format(count))

# %%
# Part 2
count = 0
curMin = len(jars)
for c in combos:
    if np.sum(c) == goal:
        if len(c) < curMin:
            curMin = len(c)
            count = 1
            continue
        elif len(c) == curMin:
            count += 1
            
print('The answer to part two is: {}'.format(count))