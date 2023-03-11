# AoC 2022 Day 20
# Challenge 1 = 4267
# Challenge 2 = 6871725358451

import os
import sys
from copy import copy

class myNum:
    def __init__(self, val) -> None:
        self.val = val

def get_input():
    f = open(os.path.join(sys.path[0], 'input.txt'), "r")
    numbers = []
    for n in f.readlines():
        numbers.append(myNum(int(n)))
        if n == '0\n':
            zero_nr = numbers[-1]
    order = copy(numbers)
    f.close()
    return numbers, order, zero_nr

def solve(loopCount, key):
    sum = 0
    numbers, order, zero_nr = get_input()
    
    for number in numbers:
        number.val *= key

    for i in range(loopCount):
        for nr in order:
            i = numbers.index(nr)
            number = numbers[i]
            if number.val == 0:
                continue
            oldPos = numbers.index(number)

            offset = abs(number.val) % (len(numbers) - 1)
            offset = -offset if number.val < 0 else offset

            newPos = oldPos + offset

            if newPos >= len(numbers):
                newPos = newPos % len(numbers) + 1
            elif newPos == 0:
                newPos = 0 if offset >= 0 else len(numbers)

            numbers.insert(newPos, numbers.pop(oldPos))
        
    zero_index = numbers.index(zero_nr)
    for i in [1000, 2000, 3000]:
        index = zero_index + i % len(numbers)
        index = index % len(numbers)
        sum += numbers[index].val

    return sum

print("p1:",solve(1,1))
print("p2:",solve(10,811589153))
