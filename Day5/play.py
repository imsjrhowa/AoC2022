# AoC 2022 Day 5
# Challenge 1 = VGBBJCRMN
# Challenge 2 = LBBVJBRMH

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

data = read_input('playinput.txt')

print(data[1][1],data[1][5])
