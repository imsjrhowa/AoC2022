# AoC 2022 Day 14
# Challenge 1 = 692
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

def printField():
    for y in range(fSize):
        for x in range(fSize):
            print(field[x+y*fSize],end="")
        print("")
    print("")

def addLine( x1,y1,x2,y2 ):
    if( x1 == x2 ):
        #Vert
        d = abs(y1-y2)+1
        for y in range( d ):
            if y2 < y1:            
                field[x1+((y1-y)*fSize)] = '#'
            else:
                field[x1+((y1+y)*fSize)] = '#'

    else:
        #horz
        d = abs(x1-x2)+1
        for x in range( d ):
            if x2 < x1:            
                field[(x1-x)+(y1*fSize)] = '#'
            else:
                field[(x1+x)+(y1*fSize)] = '#'
    
def setField(x,y,c):
    field[x+y*fSize] = c

def getField(x,y):
    return field[x+(y*fSize)]

def dropSand():
    
    dx = 500
    dy = 0

    dropMoved = True
    while( dropMoved ):

        if getField(dx,dy+1) != '.': #blocked stright down
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
            if dy >= fSize-1:
                return 1

    setField(dx,dy,'o')    
    return 0
            
data = read_input('input.txt')

fSize = 0
for line in data:
    line = line.split(" -> ")
    for p in line:
        x,y = p.split(",")
        x = int(x)
        y = int(y)
        if x>fSize:
            fSize=x
        elif y>fSize:
            fSize=y

field = []
for i in range(fSize*fSize):
    field.append(".")

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

field[50+(0*100)] = "+"

done = False
dropCount=0
while not done:
    if dropSand():
        done = True
    else:
        dropCount+=1
    #printField()

print(dropCount)