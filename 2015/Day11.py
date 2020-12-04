# 2015 Day 11

import string

data = 'hxbxwxba'

chars = string.ascii_lowercase

chars = [i for i in chars]



# Must contain one increasing straight of 3 letters
def straight(data):
    flag = False
    for idx in range(len(data)-2):
        # print("idx= "+str(idx))
        cIdx = chars.index(data[idx])
        if data[idx+1] == chars[(cIdx+1)%26] and data[idx+2] == chars[(cIdx+2)%26]:
            flag = True
        if cIdx + 2 > 25:
            flag = False
    return flag

# Must not contain i o or l
def not_contain(data):
    flag = True
    if 'i' in data or 'o' in data or 'l' in data:
        flag = False
    return flag

# must contain at least two different, non-overlapping pairs
def pairs(data):
    flag = False
    nPairs = 0
    prevValue = []
    for idx in range(len(data)-1):
        if data[idx] == data[idx+1] and data[idx] not in prevValue:
            prevValue.append(data[idx])
            nPairs += 1
    if nPairs >= 2:
        flag = True
    return flag

# Increment letters:

def increment(data):
    overflow = 0
    data = [i for i in data]
    char = data[-1]
    if char == 'z':
        data[-1] = 'a'
        overflow = 1
    else:
        data[-1] = chr(ord(data[-1])+1)
    
    idx = len(data)-2
    while overflow > 0:
        if data[idx] == 'z':
            data[idx] = 'a'
            idx -= 1
        else:
            data[idx] = chr(ord(data[idx])+overflow)
            overflow = 0
            break
    return ''.join(data)
 


data = 'hxbxwxba'

chars = string.ascii_lowercase

chars = [i for i in chars]       
    
while True:
    if straight(data) and not_contain(data) and pairs(data):
        break
    else:
        data = increment(data)
        
print(data)

data=increment(data)

while True:
    if straight(data) and not_contain(data) and pairs(data):
        break
    else:
        data = increment(data)
        
print(data)
