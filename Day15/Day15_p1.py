# AoC 2022 Day 15
# Challenge 1 = 4665948
# Challenge 2 = 13543690671045

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

data = read_input('input.txt')

Sensors = []
Beacons = []
for line in data:
    line = line.strip("Sensor at ")    
    line = line.split(": closest beacon is at ")
    line[0] = line[0].split(", ")
    line[1] = line[1].split(", ")
    sx = int(line[0][0][2:])
    sy = int(line[0][1][2:])
    bx = int(line[1][0][2:])
    by = int(line[1][1][2:])
    d = abs(sx-bx) + abs(sy-by)
    Sensors.append((sx,sy,d))
    Beacons.append((bx,by))

def valid(x,y,S):
    for (sx,sy,d) in S:
        dxy = abs(x-sx)+abs(y-sy)
        if dxy<=d:
            return False
    return True    

def p1():
    p1 = 0
    for x in range(-int(1e7),int(1e7)):
        y = int(2e6)
        if not valid(x,y,Sensors) and (x,y) not in Beacons:
            p1 += 1
    return p1

def p2():
    for (sx,sy,d) in Sensors:
        for dx in range(d+2):
            dy = (d+1)-dx
            for deltaX,deltaY in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                x = sx+(dx*deltaX)
                y = sy+(dy*deltaY)
                if not(0<=x<=int(4e6) and 0<=y<=int(4e6)):
                    continue
                assert abs(x-sx)+abs(y-sy)==d+1
                if valid(x,y,Sensors):
                    return(x*int(4e6) + y)

#print(p1())                    
print(p2())
