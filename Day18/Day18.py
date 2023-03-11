# AoC 2022 Day 18
# Challenge 1 = 4608
# Challenge 2 = 2652

import math
from collections import defaultdict
from itertools import product
import sys
import os
from collections import deque

def calc_outsideVisable( cubes, maxP ):
    count = 0
    for x in range(maxP):
        for y in range(maxP):
            for z in range(maxP):
                if (x,y,z) in cubes:
                    count+=6
                    if (x-1,y,z) in cubes:
                        count -= 1
                    if (x+1,y,z) in cubes:
                        count -= 1
                    if (x,y-1,z) in cubes:
                        count -= 1
                    if (x,y+1,z) in cubes:
                        count -= 1
                    if (x,y,z-1) in cubes:
                        count -= 1
                    if (x,y,z+1) in cubes:
                        count -= 1
    return count  

def part1():
    
    def read_input( fname, t=lambda x: x ):
        with open(os.path.join(sys.path[0], fname), "r") as f:
            contents = f.read()
            lines = contents.strip().split('\n')
        return list(map(t, lines))

    data = read_input('input.txt')

    dSet = set()
    maxP = 0
    for l in data:
        x,y,z = l.split(",")

        x = int(x)
        y = int(y)
        z = int(z)
        
        if x > maxP:
            maxP = x
        if y > maxP:
            maxP = y       
        if z > maxP:
            maxP = z            

        dSet.add((x,y,z))
    maxP += 1    

    return calc_outsideVisable(dSet, maxP)

def part2():
    def add_tuples(a, b):
        return tuple(x + y for x, y in zip(a, b))

    def read_input( fname, t=lambda x: x ):
        with open(os.path.join(sys.path[0], fname), "r") as f:
            contents = f.read()
            lines = contents.strip().split('\n')
        return list(map(t, lines))

    data = read_input('input.txt')
    pieces = {tuple(map(int, line.split(","))): 0 for line in data}

    min_coords = tuple(min(x) - 1 for x in zip(*pieces))
    max_coords = tuple(max(x) + 1 for x in zip(*pieces))

    start = deque([min_coords])
    visited = set()

    DIRECTIONS = [
        (0, 0, 1),
        (0, 1, 0),
        (1, 0, 0),
        (0, 0, -1),
        (0, -1, 0),
        (-1, 0, 0),
    ]

    while len(start) > 0:
        u = start.pop()
        if u in visited:
            continue
        visited.add(u)

        for d in DIRECTIONS:
            v = add_tuples(u, d)
            if all(a <= b <= c for a, b, c in zip(min_coords, v, max_coords)):
                if v in pieces:
                    pieces[v] += 1
                else:
                    start.append(v)

    return sum(pieces.values())

print(part1())
print(part2())