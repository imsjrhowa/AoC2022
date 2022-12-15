# AoC 2022 Day 13
# Challenge 1 = 5588
# Challenge 2 = 

import sys
import os

def read_input(fname, t=lambda x: x, strip_lines=True, force_multi=False):
    with open(os.path.join(sys.path[0], fname), "r") as f:
        contents = f.read()
    if strip_lines:
        lines = contents.strip().split('\n')
    else:
        lines = contents.split('\n')
    if len(lines) == 1 and not force_multi:
        return t(lines[0])
    return list(map(t, lines))

data = read_input('sminput.txt')

def recList( lst, rList ):
    for i in lst:
        if type(i) == list:
            rList.append(recList(i,rList))
        else:
            rList.append(i)
    return

def compare( a, b ):

    if isinstance(a, int) and isinstance(b, int):
        return a - b

    if isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            if ret := compare(x, y):
                return ret
        return len(a) - len(b)

    # check for list vs int.. and make list.
    if isinstance(a, list):
        return compare(a, [b])

    if isinstance(b, list):
        return compare([a], b)

    assert False

def compLists( a, b ):
    lst1 = eval(a)
    lst2 = eval(b)
    return compare(lst1,lst2)

#dump the space.
data = [i for i in data if i]

ans = []
index = 0
for i in range(int(len(data)/2)):
    print("Process ",i+1, end="")
    if compLists(data[index],data[index+1]) < 0:   
        ans.append(i+1)
        print(" Good")
    else:
        print("")
    index+=2

print(sum(ans))