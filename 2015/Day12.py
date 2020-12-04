# 2015 Day12

import re
import json

with open('Day12.input','r') as f:
    lines = f.read() 


# Got help from subreddit for exact re usage
print(sum(map(int, re.findall(r'-?\d+', lines))))

# Part two
def get_sum(d):
    if isinstance(d, int):
        return d
    elif isinstance(d, str):
        return 0
    elif isinstance(d, list):
        return sum(get_sum(x) for x in d)
    else:
        return 0 if any(x == 'red' for x in d.values()) else sum(get_sum(x) for x in d.values())


d = json.loads(lines)
print(get_sum(d))