# 2015 Day04

import hashlib

data = 'iwrupvqb'
# data = 'abcdef'
# data = 'pqrstuv'
number = 0
while True:
    if number%1000 == 0:
        print('Trying number = '+str(number))
    string = data + str(number)
    ha = hashlib.md5(string.encode())
    if ha.hexdigest()[0:5] == '00000':
        print('answer= '+str(number))
        break
    else:
        number += 1
        
# Part 2
data = 'iwrupvqb'
# data = 'abcdef'
# data = 'pqrstuv'
number = 0
while True:
    if number%1000 == 0:
        print('Trying number = '+str(number))
    string = data + str(number)
    ha = hashlib.md5(string.encode())
    if ha.hexdigest()[0:6] == '000000':
        print('answer= '+str(number))
        break
    else:
        number += 1
        