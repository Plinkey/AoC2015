# 2015 Day 06
import re
import numpy as np


with open('Day06.input','r') as f:
    lines = [l.rstrip('\n') for l in f]
    
lights = np.zeros((1000,1000), dtype = bool)

for line in lines:
    n = [int(x) for x in re.findall(r'\d+', line)]
    if 'on' in line:
        lights[n[0]:n[2]+1, n[1]:n[3]+1] = 1
    elif 'off' in line:
        lights[n[0]:n[2]+1, n[1]:n[3]+1] = 0
    else:
        lights[n[0]:n[2]+1, n[1]:n[3]+1] = ~lights[n[0]:n[2]+1, n[1]:n[3]+1]

print(np.sum(lights))    

# 2015 Day 06
import re
import numpy as np


with open('Day06.input','r') as f:
    lines = [l.rstrip('\n') for l in f]
    
lights = np.zeros((1000,1000), dtype = int)

for line in lines:
    n = [int(x) for x in re.findall(r'\d+', line)]
    if 'on' in line:
        lights[n[0]:n[2]+1, n[1]:n[3]+1] = 1
    elif 'off' in line:
        lights[n[0]:n[2]+1, n[1]:n[3]+1] = 0
    else:
        lights[n[0]:n[2]+1, n[1]:n[3]+1] = ~lights[n[0]:n[2]+1, n[1]:n[3]+1]

print(np.sum(lights))  