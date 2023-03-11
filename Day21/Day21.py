# AoC 2022 Day 21
# Challenge 1 = 
# Challenge 2 = 

import os
import sys

def read_input( fname, t=lambda x: x ):
    with open(os.path.join(sys.path[0], fname), "r") as f:
        contents = f.read()
        lines = contents.strip().split('\n')
    return list(map(t, lines))

data = read_input('sminput.txt')

