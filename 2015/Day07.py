# AoC 2015 Day 7


        


# %%
def parseAB(line):
    # I want to return [A,B,C]-- A or B -> C
    # At this point, wires[A] wires[B] and wires[C] all exist(if needed)
    items = line.split(' ')
    if items[0].isdigit():
        A = items[0]
    else:
        if items[0] not in wires.keys():
            return False
        else:
            A = wires[items[0]]
    if items[2].isdigit():
        B = items[2]
    else:
        if items[2] not in wires.keys():
            return False
        else:
            B = wires[items[2]]
    C = items[4]
    return [int(A),int(B),C]

def parseA(line):
    # Return [A,B]
    # Wire[A] -> wire[B]
    items = line.split(' ')
    if items[1].isdigit():
        A = items[1]
    else:
        if items[1] not in wires.keys():
            return False
        else:
            A = wires[items[1]]
    B = items[3]
    return [int(A), B]

def parseSet(line):
    items = line.split(' ')
    if items[0].isdigit():
        A = items[0]
    else:
        if items[0] not in wires.keys():
            return False
        else:
            A = wires[items[0]]
    B = items[2]
    return [int(A),B]

def andIt(idx, line):
    out = parseAB(line)
    if idx in process_later:
        process_later.pop(process_later.index(idx))
    if not out:
        process_later.append(idx)
        return
    wires[out[2]] = out[0]&out[1]
    
def orIt(idx, line):
    out = parseAB(line)
    if idx in process_later:
        process_later.pop(process_later.index(idx))
    if not out:
        process_later.append(idx)
        return
    wires[out[2]] = out[0]|out[1]
    
def rshiftIt(idx, line):
    out = parseAB(line)
    if idx in process_later:
        process_later.pop(process_later.index(idx))
    if not out:
        process_later.append(idx)
        return
    wires[out[2]] = out[0] >> out[1]
    
def lshiftIt(idx, line):
    out = parseAB(line)
    if idx in process_later:
        process_later.pop(process_later.index(idx))
    if not out:
        process_later.append(idx)
        return
    wires[out[2]] = out[0] << out[1]
    
def notIt(idx, line):
    out = parseA(line)
    if idx in process_later:
        process_later.pop(process_later.index(idx))
    if not out:
        process_later.append(idx)
        return
    answer = ~out[0]
    if answer < 0:
        answer = 2**16 + answer
    wires[out[1]] = answer
    
def setIt(idx, line):
    out = parseSet(line)
    if idx in process_later:
        process_later.pop(process_later.index(idx))
    if not out:
        process_later.append(idx)
        return
    wires[out[1]] = out[0]

#%%
with open('Day07.input','r') as f:
    lines = [l.rstrip('\n') for l in f]
    
# with open('Day07.example','r') as f:
#     lines = [l.strip('\n') for l in f]
    
process_later = []
wires = {}
    
for idx, line in enumerate(lines):
    print(idx)
    # wires['b'] = 46065 # Enable this line for part 2
    if 'AND' in line:
        andIt(idx, line)
    elif 'OR' in line:
        orIt(idx, line)
    elif 'RSHIFT' in line:
        rshiftIt(idx, line)
    elif 'LSHIFT' in line:
        lshiftIt(idx, line)
    elif 'NOT' in line:
        notIt(idx, line)
    else:
        setIt(idx, line)
        
while True:
    print(len(process_later))
    # wires['b'] = 46065 # enable this line for part 2
    if process_later == []:
        break
    for idx in process_later:
        line = lines[idx]
        if 'AND' in line:
            andIt(idx, line)
        elif 'OR' in line:
            orIt(idx, line)
        elif 'RSHIFT' in line:
            rshiftIt(idx, line)
        elif 'LSHIFT' in line:
            lshiftIt(idx, line)
        elif 'NOT' in line:
            notIt(idx, line)
        else:
            setIt(idx, line)
    
# %%

"""


def rshiftIt(idx,line):
    items = line.split(' ')
    if idx in process_later:
        process_later.pop(process_later.index(idx))
    if items[0] in wires:
        value = wires[items[0]]
        wires[items[4]] = value >> items[2]
    else:
        process_later.append(idx)
        
def lshiftIt(idx, line):
    items = line.split(' ')
    if idx in process_later:
        process_later.pop(process_later.index(idx))
    if items[0] in wires:
        value = wires[items[0]]
        wires[items[4]] = value << items[2]
    else:
        process_later.append(idx)
    
def orIt(idx, line):
    items = line.split(' ')
    if idx in process_later:
        process_later.pop(process_later.index(idx))
    if items[0] in wires and items[2] in wires:
        value1 = wires[items[0]]
        value2 = wires[items[2]]
        wires[items[4]] = value1 | value2
    else:
        process_later.append(idx)
        
def notIt(idx,line):
    items = line.split(' ')
    if idx in process_later:
        process_later.pop(process_later.index(idx))
    if items[1] in wires:
        value = wires[items[1]]
        wires[items[3]] = ~value
    else:
        process_later.append(idx)
    
def andIt(idx,line):
    items = line.split(' ')
    if idx in process_later:
        process_later.pop(process_later.index(idx))
    if items[]
"""     