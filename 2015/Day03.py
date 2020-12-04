# 2015 Day 03

with open('Day03.input','r') as f:
    line = [l.rstrip('\n') for l in f]
    
data = [char for char in line[0]]

houses = {}
x = 0 #starting point
y = 0 #starting point


for char in data:
    # Deliver
    if (x,y) in houses.keys(): #house already there
        houses[(x,y)] += 1
    else: #house not there
        houses[(x,y)] = 1
        
    # Move
    if char == '>': #move right x+=1
        x += 1
    elif char == '<': #move left, x-=1
        x -= 1
    elif char == '^': #move up, y+=1
        y += 1
    elif char == 'v': #move down, y-=1
        y -= 1


a = sum(1 for i in houses.values() if i >= 1)
print(a)
    
# Part 2

santaX = 0
santaY = 0
roboX = 0
roboY = 0

houses = {}

for idx, char in enumerate(data):
    if idx%2 == 0: # Number is even, Santa (starts at idx = 0)
        if (x,y) in houses.keys():
            houses[(santaX,santaY)] += 1
        else:
            houses[(santaX, santaY)] = 1
        if char == '>': #move right x+=1
            santaX += 1
        elif char == '<': #move left, x-=1
            santaX -= 1
        elif char == '^': #move up, y+=1
            santaY += 1
        elif char == 'v': #move down, y-=1
            santaY -= 1    
    else:
        if (x,y) in houses.keys():
            houses[(roboX,roboY)] += 1
        else:
            houses[(roboX, roboY)] = 1
        if char == '>': #move right x+=1
            roboX += 1
        elif char == '<': #move left, x-=1
            roboX -= 1
        elif char == '^': #move up, y+=1
            roboY += 1
        elif char == 'v': #move down, y-=1
            roboY -= 1  
  

a = sum(1 for i in houses.values() if i >= 1)
print(a)      