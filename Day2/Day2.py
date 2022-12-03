# AoC 2022 Day 2
# Challenge 1 = 14163
# Challenge 2 = 12091

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


# A1 Rock B2 Paper C3 Scissors
# X1 Rock Y2 Paper Z3 Scissors
winLossDict = {
    "A" : [3,6,0],
    "B" : [0,3,6],
    "C" : [6,0,3]
}

directedDict = {
    "A" : [3,4,8],
    "B" : [1,5,9],
    "C" : [2,6,7]
}

score = 0
score2 = 0
for e in data:
    op = e[0]
    me = e[2]

    score += ( winLossDict[op][ord(me) - ord('X')] + (ord(me) - ord('X')) + 1)
    score2 += ( directedDict[op][ord(me) - ord('X')])
    
print("Challenge 1 =", score)
print("Challenge 2 =", score2)