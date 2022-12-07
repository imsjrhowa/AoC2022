# AoC 2022 Day 6
# Challenge 1 = 1794
# Challenge 2 = 2851

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

def hasNoDup(string: str):
    chars = set()    
    for ch in string:
        if ch in chars:
            return False
        else:
            chars.add(ch)    
    return True

def checkMarker( e, size ):
    for i in range(len(e)-size):
        l = e[i:i+size]
        if hasNoDup(l):
            return i+size

data = read_input('input.txt')

ans1 = checkMarker(data, 4)
ans2 = checkMarker(data, 14)

print("Answer 1:", ans1)
print("Answer 2:", ans2)