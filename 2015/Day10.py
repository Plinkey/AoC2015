# 2015 Day 10

data = '1113222113'
data = '1113222113'


    
def process_digit(idx, data):
    valueOut = data[idx]
    count = 1
    while True:
        idx += 1
        if idx == len(data):
            break
        elif data[idx] == valueOut:
            count += 1
        else:
            break
    return[count,valueOut]

def process_string(data):
    data = [int(i) for i in data]
    listOut = []
    digit = 0
    while True:
        a = process_digit(digit, data)
        listOut += a
        digit += a[0]
        if digit >= len(data):
            break
    listOut = [str(i) for i in listOut]
    return ''.join(listOut)



stopIdx = 50
curIdx = 0
while curIdx < stopIdx:
    data = process_string(data)
    curIdx += 1
    
print(len(data))
