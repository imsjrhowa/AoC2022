# AoC 2022 Day 13
# Challenge 1 = 5588
# Challenge 2 = 23958

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

def compare( a, b ):

    if isinstance(a, int) and isinstance(b, int):
        return a - b

    if isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            if ret := compare(x, y):
                return ret

        # values good move to size
        return len(a) - len(b)

    # check for list vs int.. and make list.
    if isinstance(a, list):
        return compare(a, [b])

    if isinstance(b, list):
        return compare([a], b)

    assert False

#dump the space.
data = [eval(i) for i in data if i]
dividers = [[2]],[[6]]

class compareFunction:
    def __init__(self, item):
        self.item = item

    # check left
    def __lt__(self, other): 
        return compare(self.item, other.item) < 0

    # equel
    def __eq__(self, other):
        return compare(self.item, other.item) == 0

res = sorted([*data,*dividers],key=compareFunction)

ans = []
for i in range(len(res)):
    if res[i] in dividers:
        ans.append(i + 1)

print(ans[0] * ans[1])

print()