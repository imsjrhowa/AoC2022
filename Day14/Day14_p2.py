# AoC 2022 Day 14
# Challenge 1 = 
# Challenge 2 = 31706

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

def printField():
    for y in range(BASE):
        for x in range(fW):
            print(field[x+y*fW],end="")
        print("")
    print("")

def addLine( x1,y1,x2,y2 ):
    if( x1 == x2 ):
        #Vert
        d = abs(y1-y2)+1
        for y in range( d ):
            if y2 < y1:            
                field[x1+((y1-y)*fW)] = '#'
            else:
                field[x1+((y1+y)*fW)] = '#'

    else:
        #horz
        d = abs(x1-x2)+1
        for x in range( d ):
            if x2 < x1:            
                field[(x1-x)+(y1*fW)] = '#'
            else:
                field[(x1+x)+(y1*fW)] = '#'
    
def setField(x,y,c):
    field[x+y*fW] = c

def getField(x,y):
    return field[x+(y*fW)]

def dropSand():
    
    dx = 500
    dy = 0

    if getField(dx,dy) == 'o':
        return True

    dropMoved = True
    while( dropMoved ):

        if dy+1 >= fW:
            setField(dx,dy,'o')
            return False

        if getField(dx,dy+1) != '.': 
            if getField(dx-1,dy+1) == '.':
                dx -= 1
                dy += 1
            elif getField(dx+1,dy+1) == '.':
                dx += 1
                dy += 1
            else:
                dropMoved = False
        else:
            dy += 1
            if dy >= fW-1:
                setField(dx,dy,'o')
                dropMoved = False
                return False

        if dy == fW:
            dropMoved = False

    setField(dx,dy,'o')
    return False

data = read_input('input.txt')

BASE= 0
fW = 0
for line in data:
    line = line.split(" -> ")
    for p in line:
        x,y = p.split(",")
        x = int(x)
        y = int(y)
        if x>fW:
            fW=x
        elif y>BASE:
            BASE=y

fW = fW*2 
BASE = BASE + 2

field = []

for i in range(fW*fW):
    field.append(".")

for i in range(fW):
    field[i+BASE*fW] = '#'

for line in data:
    line = line.split(" -> ")
    sx = None
    sy = None
    for p in range(len(line)):
        x,y = line[p].split(",")
        x = int(x)
        y = int(y)
        if sx == None:
            sx = x
            sy = y
        else:
            addLine( sx,sy, x,y )
            sx = x
            sy = y

field[500] = "+"

done = False
dropCount=0
while not done:
    if dropSand():
        done = True
    else:
        dropCount+=1

print(dropCount)