# AoC 2022 Day 9
# Challenge 1 = 6269
# Challenge 2 = 2557

import sys
import os
import math

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

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, x, y):
        new_node = Node(x,y)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    def print_list(self):
        cur = self.head
        while cur:
            if cur == self.head:
                print("H",cur.x, cur.y)
            elif cur.next == None:
                print("T",cur.x, cur.y)                
            else:
                print("-",cur.x, cur.y)                

            cur = cur.next

    def get_count(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count            

    def get_data(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
            if not cur:
                return None
        return cur.x,cur.y

    def get_prev_data(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
            if not cur:
                return None
        if cur.prev:
            return cur.prev.x, cur.prev.y
        return None


    def set_data(self, index, x, y ):
        cur = self.head
        for i in range(index):
            cur = cur.next
            if not cur:
                return None
        
        cur.x = x
        cur.y = y


llist = LinkedList()
for i in range(10):
    llist.append(0,0)

data = read_input('input.txt')

visit = []
def moveHead(dx,dy):

    for i in range(llist.get_count()-1):
        hx, hy = llist.get_data(i)
        tx, ty = llist.get_data(i+1)

        if i == 0: # head is the only guy that moves..
            hx += dx
            hy += dy
        
        llist.set_data(i,hx,hy)

        d = math.sqrt((hx - tx)**2 + (hy - ty)**2)

        if d >= 2:
 
            _dx = (hx - tx)
            _dy = (hy - ty)

            if abs(_dx) > 1:
                if _dx < 0:
                    _dx+=1
                elif _dx > 0:
                    _dx-=1

            if abs(_dy) > 1:
                if _dy < 0:
                    _dy+=1
                elif _dy > 0:
                    _dy-=1

            tx += _dx
            ty += _dy

            llist.set_data(i+1,tx,ty)

    tailx, taily = llist.get_data(9)
    if [tailx,taily] not in visit:
        visit.append([tailx,taily])              
       

def printShowMap():
    displaySize = 15

    display = []
    for x in range(-displaySize,displaySize):
        for y in range(-displaySize,displaySize):
            display.append('.')

    
    for x,y in visit:
        display[x+(y*displaySize*2)] = '*'

    c = 0
    for i in range(llist.get_count()):
        x,y = llist.get_data(i)
        if c == 0:
            display[x+(y*(displaySize*2))] = 'H'
        elif c == 9:
            display[x+(y*(displaySize*2))] = 'T'
        else:
            display[x+(y*(displaySize*2))] = c
        c+=1

    for x in range(-displaySize,displaySize):
        for y in range(-displaySize,displaySize):
            print(display[y+(x*(displaySize*2))],end="")
        print("")


for c in data:
    d, l = c.split(' ')

    for i in range(int(l)):
        if d == 'U':
            moveHead(0,-1)
        elif d == 'D':
            moveHead(0,1)
        elif d == 'R':
            moveHead(1,0)
        elif d == 'L':
            moveHead(-1,0)

print( len(visit) )