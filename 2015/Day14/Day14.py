debug = False


if debug:
    with open('Day14.example', 'r') as f:
        data = f.read().splitlines()
else:    
    with open('Day14.input', 'r') as f:
        data = f.read().splitlines()
        

    
# %%
# Parse out code
deerDict = {}
for l in data:
    ll = l.split(' ')
    [deer, speed, mtime, rtime] = ll[0], int(ll[3]), int(ll[6]), int(ll[13])
    deerDict[deer] = {'speed':speed, 'mtime':mtime, 'rtime':rtime}

# %%
# Fly function
def fly(deer, t):
    """ Fly for t seconds, return distance traveled"""
    dist = 0
    curTime = 0
    flags = (['m'] * deer['mtime']) + (['r']*deer['rtime'])
    while True:
        if flags[curTime % len(flags)] == 'm':  # Move second
            dist += deer['speed']
            curTime += 1
        elif flags[curTime % len(flags)] == 'r':  # rest second
            curTime += 1
            
        if curTime >= t:
            break
    return dist

# %% 
# Part 1 answers
if debug:
    totalT = 1000
else:
    totalT = 2503

distances = []
for d in deerDict:
    distances.append(fly(deerDict[d],totalT))
    
print('Answer Part ONE: {}'.format(max(distances)))

# %%

def points(endT):
    deerPos = {}
    deerPoints = {}
    for t in range(endT+1):
        if t == 0:
            continue
        if debug:
            print('############# THE CURRENT TIME IS {}'.format(t))
        # Figure out distance travled
        for d in deerDict:
            deerPos[d] = fly(deerDict[d],t)
        # Awared points
        max_value = max(deerPos.values())
        pointsTo = [k for k,v in deerPos.items() if v == max_value]
        if debug:
            print(pointsTo)
        for winner in pointsTo:
            if winner not in deerPoints.keys():
                deerPoints[winner] = 0
            deerPoints[winner] += 1
            if debug:
                print('Deer Position {}'.format(deerPos))
                print('Deer Points {}'.format(deerPoints))
    return deerPoints

a = points(totalT)
print('Answer Part TWO: {}'.format(max(a.values())))
