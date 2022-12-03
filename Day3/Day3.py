# AoC 2022 Day 3
# Challenge 1 = 8233
# Challenge 2 = 2821

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

def findSim( a, b ):
    for c1 in a:
        for c2 in b:
            if c1 == c2:
                return c1
    return ''

def scoreOut( o ):
    v = ord(o)
    if v >= 97:
        return v-96
    else:
        return (v-65) + 27

def findSim3( a, b, c ):
    for c1 in a:
        for c2 in b:
            for c3 in c:
                if c1 == c2 and c1 == c3:
                    return c1
    return ''

score = 0
score2 = 0
for string in data:
    l = len(string) / 2 
    firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
        
    firstpart = ''.join(sorted(firstpart))
    secondpart = ''.join(sorted(secondpart))

    out = findSim( firstpart, secondpart )
    if out != '':
        score += scoreOut(out)

while len(data):
    out = findSim3(data[0],data[1],data[2])
    if out != '':
        score2 += scoreOut(out)
    del data[:3]

print("Challenge 1 =", score)
print("Challenge 2 =", score2)