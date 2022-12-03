# AoC 2022 Day 1
# C1 72718
# C2 213089

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

data = read_input('Input.txt')
R = []
R.append(0)

for ele in data:
    if len(ele) > 0:
        R[len(R)-1] += int(ele)
    else:
        R.append(0)

R.sort(reverse=True)

print("Challenge 1 =", R[0])

print("Challenge 2 =", R[0] + R[1] + R[2])