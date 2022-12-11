# AoC 2022 Day 10
# Challenge 1 = 17180
# Challenge 2 = REHPRLUB

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

regX = 1
cycle = 0
signal = 0

print()

def tick():
    global signal, cycle
    cycle += 1
    if cycle%40 == 20:
        signal += cycle * regX

def tick2():
    global signal, cycle

    if cycle%40 in ( regX-1, regX, regX+1 ):        
        print("#",end="")
    else:
        print(".",end="")

    cycle += 1
    if cycle%40==0:
        print()


for line in data:
    line = line.split();

    if 'noop' in line: 
        tick2()
    elif 'addx' in line:
        tick2()
        tick2()
        regX += int(line[1])

print(signal) # Challenge 1 only.