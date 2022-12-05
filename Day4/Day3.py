# AoC 2022 Day 4
# Challenge 1 = 573
# Challenge 2 = 876

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

def contains( f, s ):
    f1, f2 = f.split('-')
    s1, s2 = s.split('-')
    f1 = int(f1)
    f2 = int(f2)
    s1 = int(s1)
    s2 = int(s2)

    df = abs(f1-f2)
    ds = abs(s1-s2)
    if df >= ds:
        if f1 <= s1 and f2 >= s2:
            return 1
    else:
        if s1 <= f1 and s2 >= f2:
            return 1

    return 0

def overlaps( f,s ):
    f1, f2 = f.split('-')
    s1, s2 = s.split('-')
    f1 = int(f1)
    f2 = int(f2)
    s1 = int(s1)
    s2 = int(s2)

    if f1 < s1:
        if f2 >= s1:
            return 1
    else:
        if s2 >= f1:
            return 1

    return 0

data = read_input('Input.txt')
score = 0
score2 = 0

for p in data:
    f, s = p.split(',')

    # 1
    if contains( f,s ) > 0:
        score += 1

    # 2
    if contains( f,s ) > 0:
        score2 += 1
    elif overlaps( f,s ) > 0:
        score2 += 1

print("Challenge 1 =", score)
print("Challenge 2 =", score2)