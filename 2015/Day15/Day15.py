debug = False

# %% Imports
import re
import numpy as np
import itertools

# %% Load Data
if debug:
    with open('Day15.example', 'r') as f:
        data = f.read().splitlines()
else:    
    with open('Day15.input', 'r') as f:
        data = f.read().splitlines()
        
        
# %%
# Parse
ingredients = {}
for line in data:
    items = re.split(': |,',line)
    items = [i.lstrip(' ') for i in items]
    for i in items:
        ingredients[items[0]] = {f.split(' ')[0]: int(f.split(' ')[1]) for f in items[1:]}
        
# %% 
# Function to return score for individual parameters
def calcParam(elem, amounts):
    total = 0
    for idx, ing in enumerate(ingredients):
        v = ingredients[ing][elem]
        total += v*amounts[idx]
    if total < 0:
        return 0
    else:
        return total
        
    


# %%
# Score function for Part 1
def score(amounts):
    params = ['capacity', 'durability', 'flavor', 'texture', 'calories']
    cap = calcParam('capacity', amounts)
    dur = calcParam('durability', amounts)
    fla = calcParam('flavor', amounts)
    tex = calcParam('texture', amounts)
    return cap * dur * fla * tex
    
    

        
# %%
# This cell was my original algo replaced by above
# It gives same answers.  Correct for example, wrong for input
    
# def score(amounts):
#     scores = [0,0,0,0]
#     counter = 0
#     for ingr in ingredients:
#         for idx, param in enumerate(ingredients[ingr]):
#             if param == 'calories':
#                 continue
#             else:
#                 scores[idx] += ingredients[ingr][param] * amounts[counter]
#         counter += 1
#     if any(ele < 0 for ele in scores):
#         return 0
#     # print('With Amounts: {} Scores: {} Product: {}'.format(amounts,scores, np.prod(scores)))
#     return np.prod(scores)
            
# %% Maximize function for part 1

def maximize():
    curMax = 0
    outputs = []
    for amounts in itertools.combinations_with_replacement(list(range(0,101)), len(ingredients)):
        if np.sum(amounts) == 100:
            curMax = max(curMax, score(amounts))
    return curMax
    
    
# print('The answer to part one is: {}'.format(maximize()))
# NOTE: 19150560 is too low
a = maximize()
print(a)