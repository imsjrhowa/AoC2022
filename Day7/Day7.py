# AoC 2022 Day 7
# Challenge 1 = 2031851
# Challenge 2 = 2568781

import sys
import os
from collections import defaultdict
from pathlib import Path

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

cwd = Path("/")
dirs = defaultdict(int)

for line in data:
    nline = line.split()
    if nline[0] == '$' and nline[1] == 'cd':
        newdir = nline[2]
        cwd = cwd / newdir #join
        cwd = cwd.resolve()
    elif nline[0].isdigit():
        size = int(nline[0])
        for path in [cwd, *cwd.parents]:
            dirs[path] += size

answer1 = 0
for x in dirs.values():
    if x <= 100000:
        answer1 += x

answer2 = 0
rx = dirs[Path("C:/")] # root size
need = 30000000 - (70000000 - rx)
sizes = []
for x in dirs.values():
    sizes.append(x)

sizes.sort()

for size in sizes:
    if size >= need:
        answer2 = size
        break

print("Answer 1:", answer1 )
print("Answer 1:", answer2 )