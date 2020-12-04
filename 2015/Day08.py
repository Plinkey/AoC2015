
    
with open('Day08.input','r') as f:
    lines = [l.strip('\n') for l in f]


import fileinput
import ast
import re

chars = 0
lits = 0
encoded_chars = 0

for line in lines:
    chars += len(line)
    lits += len(ast.literal_eval(line))
    encoded_chars += (len(re.escape(line)))

print(chars-lits)
print(encoded_chars - chars)
    

t = 0
for l in lines:
    t += 2
    for s in l:
        if s == '\\' or s == '"':
            t += 1
print(t)