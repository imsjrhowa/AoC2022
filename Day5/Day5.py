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

data = read_input('input.txt')

# sm_input
# stacks = {
#     1 : [' ','Z','N'],
#     2 : [' ','M','C','D'],
#     3 : [' ','P'],
# }


# [Q] [J]                         [H]
# [G] [S] [Q]     [Z]             [P]
# [P] [F] [M]     [F]     [F]     [S]
# [R] [R] [P] [F] [V]     [D]     [L]
# [L] [W] [W] [D] [W] [S] [V]     [G]
# [C] [H] [H] [T] [D] [L] [M] [B] [B]
# [T] [Q] [B] [S] [L] [C] [B] [J] [N]
# [F] [N] [F] [V] [Q] [Z] [Z] [T] [Q]
#  1   2   3   4   5   6   7   8   9 

stacks = {
    1 : [' ','F','T','C','L','R','P','G','Q'],
    2 : [' ','N','Q','H','W','R','F','S','J'],
    3 : [' ','F','B','H','W','P','M','Q'],
    4 : [' ','V','S','T','D','F'],
    5 : [' ','Q','L','D','W','V','F','Z'],
    6 : [' ','Z','C','L','S'],
    7 : [' ','Z','B','M','V','D','F'],
    8 : [' ','T','J','B'],
    9 : [' ','Q','N','B','G','L','S','P','H'],
}

def move( dict, number, fromStack, toStack ):
    hold = []
    for i in range(number):
        hold += ( dict[fromStack].pop() )

    for i in range(number):
        dict.setdefault(toStack,).append(hold[i])
    return dict

def movev2( dict, number, fromStack, toStack ):
    hold = []
    for i in range(number):
        hold += ( dict[fromStack].pop() )

    hold.reverse()

    for i in range(number):
        dict.setdefault(toStack,).append(hold[i])
    return dict

for str in data:
    w = str.split(' ')
    ## Challeng 1
    #stacks = move(stacks, int(w[1]), int(w[3]), int(w[5]) )
    ## Challeng 2
    stacks = movev2(stacks, int(w[1]), int(w[3]), int(w[5]) )

ans = []
for i in range(1,10):
    ans.append(stacks[i][len(stacks[i])-1])

print("Answer =", ''.join(ans))