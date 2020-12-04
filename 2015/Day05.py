# 2015 day 5


with open('Day05.input','r') as f:
    lines = [l.rstrip('\n') for l in f]
    

niceCount = 0
for line in lines:
    vowelCount = 0
    vowelFlag = False
    
    vowelCount += line.count('a')
    vowelCount += line.count('e')
    vowelCount += line.count('i')
    vowelCount += line.count('o')
    vowelCount += line.count('u')
    
    if vowelCount >= 3:
        vowelFlag = True
    
    doubleFlag = False
    for idx, char in enumerate(line):
        if idx < len(line)-1:
            if line[idx+1] == char:
                doubleFlag = True
                break
        
    excludeFlag = True # False means they are not present
    if any(x in line for x in ['ab','cd','pq','xy']):
        excludeFlag = False
        
    if vowelFlag and doubleFlag and excludeFlag:
        niceCount += 1
        
        
lower_case = list(map(chr, range(65+32, 65+32+26)))


# Part two
pairs = [a + b for a in lower_case for b in lower_case]
triples = [a + b + a for a in lower_case for b in lower_case]


def is_nice_2(w):
    return any(w.count(p) > 1 for p in pairs) and any(t in w for t in triples)


print(sum(map(is_nice_2, lines)))
