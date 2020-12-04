# Day 02


with open('Day02.input','r') as f:
    lines = [l.rstrip('\n') for l in f]

packages = []
for line in lines:
    present = [int(i) for i in line.split('x')]
    packages.append(present)
    
total = 0
for package in packages:
    # package = [2,3,4]
    l = package[0]
    w = package[1]
    h = package[2]
    
    a = l*w
    b = w*h
    c = l*h
    
    total += 2*a+2*b+2*c+min(a,b,c)
    
    
# Part 2
    
lenRibbon = 0
for package in packages:
    # package = [4,2,3]
    package.sort()
    smallest = package[0]
    middle   = package[1]
    big      = package[2]
    bow = smallest*middle*big
    perim = 2*smallest + 2*middle
    lenRibbon += bow + perim
