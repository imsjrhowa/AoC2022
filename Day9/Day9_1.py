# AoC 2022 Day 9
# Challenge 1 = 6269
# Challenge 2 = 2557

import sys
import os
import math

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

hx = 0
hy = 0
tx = 0
ty = 0

visit = []
def moveHead(dx,dy):
    global hx
    global hy
    global tx
    global ty
    ohx = hx
    ohy = hy
    hx += dx
    hy += dy
    d = math.sqrt((hx - tx)**2 + (hy - ty)**2)
    if d >= 2:
        tx = ohx
        ty = ohy
        if [tx,ty] not in visit:
            visit.append([tx,ty])


for c in data:
    d, l = c.split(' ')
    for i in range(int(l)):
        if d == 'U':
            moveHead(0,-1)
        elif d == 'D':
            moveHead(0,1)
        elif d == 'R':
            moveHead(1,0)
        elif d == 'L':
            moveHead(-1,0)

print( len(visit) )