# 2015 Day09.py

from itertools import permutations

with open('Day09.input') as f:
    lines = [l.strip().split() for l in f.readlines()]
    

paths = {}
for l in lines:
    paths[l[0], l[2]] = int(l[4])
    paths[l[2], l[0]] = int(l[4]) #same distance in return trip

places = list(set(l[0] for l in paths.keys()))

#part 1
shortest = float('inf')

for p in permutations(places):
    length = 0
    for idx in range(len(p)-1):
        length += paths[p[idx],p[idx+1]]
    shortest = min(shortest,length)
        
print( shortest)


# Part 2
longest = 0

for p in permutations(places):
    length = 0
    for idx in range(len(p)-1):
        length += paths[p[idx],p[idx+1]]
    longest = max(longest, length)
    
print(longest)

