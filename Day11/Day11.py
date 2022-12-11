# AoC 2022 Day 11
# Challenge 1 = 54054
# Challenge 2 = 14314925001

import sys
import os
import math

class monkey:
    def __init__(self, name, items, op, test, tt, tf ):
        self.name = name
        self.items = items # list
        self.op = op # string
        self.test = test
        self.tt = tt
        self.tf = tf
        self.inspect = 0

monkeys = []

# SAMPLE
# monkeys.append( monkey(0,       [79,98], "o*19", 23, 2, 3) )
# monkeys.append( monkey(1, [54,65,75,74],  "o+6", 19, 2, 0) )
# monkeys.append( monkey(2,  [79, 60, 97],  "o*o", 13, 1, 3) )
# monkeys.append( monkey(3,          [74],  "o+3", 17, 0, 1) )
# MOD_List = (23*19*13*17)

# DATA
monkeys.append( monkey(0,                   [74, 64, 74, 63, 53], "o*7",  5, 1, 6) )
monkeys.append( monkey(1,                       [69, 99, 95, 62], "o*o", 17, 2, 5) )
monkeys.append( monkey(2,                               [59, 81], "o+8",  7, 4, 3) )
monkeys.append( monkey(3,           [50, 67, 63, 57, 63, 83, 97], "o+4", 13, 0, 7) )
monkeys.append( monkey(4,       [61, 94, 85, 52, 81, 90, 94, 70], "o+3", 19, 7, 3) )
monkeys.append( monkey(5,                                   [69], "o+5",  3, 4, 2) )
monkeys.append( monkey(6,                           [54, 55, 58], "o+7", 11, 1, 5) )
monkeys.append( monkey(7,               [79, 51, 83, 88, 93, 76], "o*3",  2, 0, 6) )
MOD_List = (5*17*7*13*19*3*11*2)

__part2__ = True

rounds = 20

if __part2__:
    rounds = 10000

for r in range(rounds):
    if r in [1,5,10,15,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]:
        mbusiness = []
        for m in monkeys:
            mbusiness.append(m.inspect)
        mbusiness.sort(reverse=True)
        print( mbusiness[0] * mbusiness[1])

    for mIndex in range(len(monkeys)):    
        itemList = monkeys[mIndex].items.copy()
        for itemIndex in range(len(itemList)):
            monkeys[mIndex].inspect += 1
            ret = 0
            op = monkeys[mIndex].op
            parsedOp = op.replace("o", str(itemList[itemIndex]))
            del monkeys[mIndex].items[0]

            if "*" in parsedOp: #multiply
                parsedOp = parsedOp.split("*")
                #part 2
                if __part2__:
                    opValueL = int(parsedOp[0]) % MOD_List
                    opValueR = int(parsedOp[1]) % MOD_List
                else:
                    opValueL = int(parsedOp[0])
                    opValueR = int(parsedOp[1])

                ret = opValueL * opValueR
            elif "+" in parsedOp:
                parsedOp = parsedOp.split("+")
                #part 2
                if __part2__:
                    opValueL = int(parsedOp[0]) % MOD_List
                    opValueR = int(parsedOp[1]) % MOD_List
                else:
                    opValueL = int(parsedOp[0])
                    opValueR = int(parsedOp[1])
                ret = opValueL + opValueR

            # part 1
            if not __part2__:
                ret = math.floor(ret / 3)
    
            if ret%monkeys[mIndex].test == 0:
                monkeys[monkeys[mIndex].tt].items.append(ret)
            else:
                monkeys[monkeys[mIndex].tf].items.append(ret)

mbusiness = []
for m in monkeys:
    mbusiness.append(m.inspect)

mbusiness.sort(reverse=True)
print("Answer", mbusiness[0] * mbusiness[1])