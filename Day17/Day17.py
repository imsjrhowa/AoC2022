# AoC 2022 Day 17
# Challenge 1 = 3227
# Challenge 2 = 1597714285698 ( have not entered yet.. was taken from another code )

import math
from collections import defaultdict
import sys
import os
import time

def part1():
    
# |..@X@@.|
# |.......|

    shape1 = [ (0,0),(-1,0),(1,0),(2,0) ]

# |...@...|
# |..@@@..|
# |...X...|

    shape2 = [ (0,0),(0,-1),(-1,-1),(1,-1),(0,-2) ]

# |....@..|
# |....@..|
# |..@X@..|

    shape3 = [ (0,0),(-1,0),(1,0),(1,-1),(1,-2) ]

# |..@....|
# |..@....|
# |..@....|
# |..Xs...|

    shape4 = [ (-1,0),(-1,-1),(-1,-2),(-1,-3) ]

# |..@@...|
# |..@X...|

    shape5 = [ (0,0),(-1,0),(-1,-1),(0,-1) ]

    current_shape = 0
    shapes = [ shape1,shape2,shape3,shape4,shape5 ]

    def read_input( fname, t=lambda x: x ):
        with open(os.path.join(sys.path[0], fname), "r") as f:
            contents = f.read()
            lines = contents.strip().split('\n')
        return list(map(t, lines))

    data = read_input('input.txt')

    field = []

    for i in range(9*9):
        field.append('.')

    for x in range(9):
        for y in range(9):
            if x == 0 or x == 8:                
                field[x+y*9] = '|'
            elif y == 8:
                field[x+y*9] = '_'


    objSet = set()

    for i in range(1,8):
        objSet.add((i,0))

    jet = []
    jetIndex = 0
    for i in range(len(data[0])):
        jet.append(data[0][i])

    spawn = True
    spawnCount = 0
    max_height = 0

    while spawnCount <= 1000000000000:
        # spawn
        if spawn:
            max_height = int(1e17)
            for i in objSet:
                if i[1] < max_height:
                    max_height = i[1]

            print(time.perf_counter(),spawnCount,abs(max_height))

            shape = shapes[current_shape]
            current_shape += 1
            if current_shape >= len(shapes):
                current_shape = 0

            loc = (4,max_height-4)
            spawn = False
            spawnCount += 1
            if spawnCount > 1000000000000:
                break;

        #jets
        c = jet[jetIndex]
        jetIndex+=1
        if jetIndex >= len(jet):
            jetIndex = 0

        jetLoc = (0,0)
        if c == '<':
            jetLoc = (loc[0]-1,loc[1])    
        else:
            jetLoc = (loc[0]+1,loc[1])

        blocked = False
        for i in range(len(shape)):
            p = (jetLoc[0]+shape[i][0],jetLoc[1]+shape[i][1])
            if p in objSet or p[0] <= 0 or p[0] >= 8:
                blocked = True

        if blocked == False:
            loc = jetLoc
                
        #move
        blocked = False
        moveLoc = (loc[0],loc[1]+1)
        for i in range(len(shape)):
            p = (moveLoc[0]+shape[i][0],moveLoc[1]+shape[i][1])
            if p in objSet:
                for i in range(len(shape)):
                    place = (loc[0]+shape[i][0],loc[1]+shape[i][1])
                    objSet.add(place)
                    blocked = True
                    spawn = True
                break;
        if blocked == False:
            loc = moveLoc

    # for p in objSet:
    #     x = p[0]
    #     y = abs(p[1])
    #     field[x+y*9] = '#'

    # for y in range(9):
    #     for x in range(9):
    #          print(field[x+y*9],end="")
    #     print("")
    # print("")

    return abs( max_height )
    
print(part1())