import re

f = open('input.txt')

res = 0

LETTER_TO_NUM =  {
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
        }

def to_int(d):
    if d.isdigit():
        return int(d)
    else:
        return LETTER_TO_NUM[d]

for i,l in enumerate(f):
    m =  [None, None]
    x = re.search('(one|two|three|four|five|six|seven|eight|nine|[0-9])', l)
    m[0] = l[x.start():x.end()] 
    n = len(l)
    for i in range(n-1,-1,-1):
        x = re.match('(one|two|three|four|five|six|seven|eight|nine|[0-9])', l[i:n])
        if x is not None:
            m[1] = l[i:n][x.start():x.end()]
            break

    res += int(str(to_int(m[0]))+str(to_int(m[1])))

print(res)