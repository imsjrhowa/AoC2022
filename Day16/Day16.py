# AoC 2022 Day 16
# Challenge 1 = 1792
# Challenge 2 = 
import math
from collections import defaultdict
import sys
import os

def part1():
    valves = {}
    dist = defaultdict(lambda: defaultdict(lambda: math.inf))

    def read_input( fname, t=lambda x: x ):
        with open(os.path.join(sys.path[0], fname), "r") as f:
            contents = f.read()
            lines = contents.strip().split('\n')
        return list(map(t, lines))

    data = read_input('input.txt')

    # parse data
    for line in data:
        line = line.split(" ")
        valve = line[1] # name
        
        rate = line[4] # rate
        rate = rate[5:]
        rate = rate.strip(";")
        rate = int(rate)
        valves[valve] = int(rate)

        del line[0:9:1] # joining rooms
        for b in range(len(line)):
            if "," in line[b]:
                line[b] = line[b][:-1]

        dist[valve][valve] = 0 # self
        
        for c in line:
            dist[valve][c] = 1

    for a in valves:
        for b in valves:
            for c in valves:
                dist[b][c] = min(dist[b][c], dist[b][a] + dist[a][c])
 
    def process(i, t, valveRooms):
        ret = 0
        for j in valveRooms:
            # time - move - turn on >= zero
            if (t - dist[i][j] - 1) >= 0:
                time_left = t - dist[i][j] - 1
                ret = max(ret, valves[j] * time_left + process(j, time_left, valveRooms - {j}))
        return ret

    valveRooms = set()
    for l in valves:
         if valves[l] > 0:
            valveRooms.add(l)

    return process("AA", 30, valveRooms)

print(part1())