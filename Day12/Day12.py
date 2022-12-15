# AoC 2022 Day 12
# Challenge 1 = 447
# Challenge 2 = 446

import sys
import os
from collections import deque

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

###############################################################################
def challenge1():
    grid = { (x, y): c for x, row in enumerate(data) 
                       for y, c in enumerate(row) }

    start = 0
    for k, v in grid.items():
        if v == "S":
            start = k
            break

    end = 0
    for k, v in grid.items():
        if v == "E":
            end = k
            break

    # set start and end to be values that we care about a-z
    grid[start] = "a"
    grid[end] = "z"

    visit = {}
    Q = deque([(0, start)])

    while len(Q) > 0:
        steps, p = Q.popleft()
        
        if p in visit:
            continue
        
        visit[p] = steps

        for loc in [(p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)]:
            p1 = ord(grid.get(loc, "~"))
            p2 = ord(grid[p]) # my current loc
            if p1 - p2 > 1: # one step up only.
                continue

            Q.append((steps + 1, loc))

    return visit[end]

###############################################################################

def tryLocation( grid, _p, _end ):
    visit = {}
    Q = deque([(0, _p)])

    while len(Q) > 0:
        steps, p = Q.popleft()
        
        if p in visit:
            continue

        visit[p] = steps

        for loc in [(p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1)]:
            p1 = ord(grid.get(loc, "~"))
            p2 = ord(grid[p]) # my current loc
            if p1 - p2 > 1: # one step up only.
                continue

            Q.append((steps + 1, loc))

    if _end in visit:
        return visit[_end]
    return sys.maxsize # trapped? never found end point?

def challenge2():
    grid = { (x, y): c for x, row in enumerate(data) 
                       for y, c in enumerate(row) }

    start = 0
    for k, v in grid.items():
        if v == "S":
            start = k
            break

    end = 0
    for k, v in grid.items():
        if v == "E":
            end = k
            break

    # set start and end to be values that we care about a-z
    grid[start] = "a"
    grid[end] = "z"
    
    tryList = []
    for k,v in grid.items():
        if v == 'a':
            tryList.append(k)

    results = []
    for t in tryList:
        results.append(tryLocation(grid,t,end))

    results.sort()
    return results[0]

print("A1:",challenge1())
print("A2:",challenge2())
