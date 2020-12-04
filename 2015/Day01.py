#2015 day 1

with open('Day01.input','r') as f:
    line = [l.rstrip('\n') for l in f]
    
data = [char for char in line[0]]


curFloor = 0
for char in data:
    if char == '(':
        curFloor += 1
    elif char == ')':
        curFloor -= 1
        
print(curFloor)


#####
# part 2

curFloor = 0
for idx, char in enumerate(data):
    if char == '(':
        curFloor += 1
    elif char == ')':
        curFloor-= 1
    if curFloor < 0:
        print(idx+1)
        break