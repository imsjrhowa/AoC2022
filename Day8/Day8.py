# AoC 2022 Day 8
# Challenge 1 = 1711
# Challenge 2 = 301392

import sys
import os

__firstChallenge__ = True

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

#global
map = []
w = h = len(data)
seenMap = []

def placeSeen( x, y, value ):
    seenMap[x+(y*h)] = value

def setMapValue(x,y,value):
    map[x+(y*h)] = value

def getMapValue(x,y,mapToUse):
    return mapToUse[x+(y*h)]

def printMap():
    for x in range(w):
        for y in range(h):
            print(map[y+(x*h)],end="")
        print("")
    print("")

def printSeenMap():
    for x in range(w):
        for y in range(h):
            print(seenMap[x+(y*h)],end="")
        print("")
    print("")

for line in data:
    for i in range(len(line)):
        map.append(int(line[i]))
        seenMap.append(0)

dirs = [[-1,0],[1,0],[0,-1],[0,1]]

def checkDir(x,y,dx,dy):
    c = getMapValue(x,y,map)
    for i in range(w):
        nx = x+dx
        ny = y+dy
        if nx >= 0 and ny >= 0 and nx < w and ny < h:
            v = getMapValue(nx,ny,map)
            if v >= c:
                return False
        else:
            return True # we can always see the edge.
        x = nx
        y = ny

    return True
    
def checkValueDir(x,y,dx,dy):
    c = getMapValue(x,y,map)
    score = 0
    for i in range(w):
        nx = x+dx
        ny = y+dy
        if nx >= 0 and ny >= 0 and nx < w and ny < h:
            v = getMapValue(nx,ny,map)
            score += 1
            if v >= c:
                return score
        else:
            return score
        x = nx
        y = ny

    return score
    
if __firstChallenge__:
    # challenge 1    
    for x in range(0,w):
        for y in range(0,h):
            if ( checkDir(x,y,dirs[0][0],dirs[0][1]) or
                checkDir(x,y,dirs[1][0],dirs[1][1]) or
                checkDir(x,y,dirs[2][0],dirs[2][1]) or
                checkDir(x,y,dirs[3][0],dirs[3][1]) ):
                placeSeen(x,y,1)

    print( sum( v for v in seenMap if v > 0 ) )
else:
    # challenge 2
    for x in range(1,w-1):
        for y in range(1,h-1):
        
            v1 = checkValueDir(x,y,dirs[0][0],dirs[0][1])
            v2 = checkValueDir(x,y,dirs[1][0],dirs[1][1])
            v3 = checkValueDir(x,y,dirs[2][0],dirs[2][1])
            v4 = checkValueDir(x,y,dirs[3][0],dirs[3][1])

            placeSeen(x,y,v1*v2*v3*v4)

    seenMap.sort(reverse=True)
    print(seenMap[0])