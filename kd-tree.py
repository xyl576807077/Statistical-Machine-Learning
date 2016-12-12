# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:08:47 2016

@author: Administrator
"""
from Queue import PriorityQueue
import math
#input = [[6.27,5.50],[1.24,-2.86],[17.05,-12.79],
#         [-6.88,-5.40],[-2.96,-0.50],[7.75,-22.68],
#         [10.80,-5.03],[-4.60,-10.55],[-4.96,12.61],
#         [1.75,12.26],[15.31,-13.16],[7.83,15.70],
#         [14.63,-0.35]]
input = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]
maxsize = 1
pq = PriorityQueue(maxsize=maxsize)
looking = [2.1, 3.1]
class Res(object):
    def __init__(self, distance, node):
        self.distance = distance
        self.node = node
        return
    
    def __cmp__(self, other):
        if self.distance > other.distance:
            return 0
        else:
            return 1

class KDTree(object):
    def __init__(self, node, split, f, deepth, l = None, r = None):
        self.node = node
        self.split = split
        self.l = l
        self.r = r
        self.f = f
        self.deepth = deepth
    
def buildKDTree(L, s, f, deepth):
    if len(L) == 0:
        return None
    s %= 2
    L = sorted(L, key = lambda x:x[s])
    mid = len(L)/2-1 if len(L) %2 == 0 else len(L)/2 
    node = L[mid]
    Node = KDTree(node, s%2, f, deepth)
    Node.l = buildKDTree(L[:mid], s+1, Node, deepth+1)
    Node.r = buildKDTree(L[mid+1:], s+1, Node, deepth+1)
    Node.f = f
    return Node
    
def search(Node):
    split = Node.split
    if Node.node[split] > looking[split]:
        if Node.l == None:
            return Node
        else:
            return search(Node.l)
    else:
        if Node.r == None:
            return Node
        else:
            return search(Node.r)
            
def cal(node1, node2):
    dimenssion = len(node1)
    tmp = 0
    for i in range(dimenssion):
        tmp += (node1[i]-node2[i]) ** 2
    return math.sqrt(tmp)

def solve(Node):
    current = search(Node)
    while current.f != None:
        print current.node
        splitDistance = abs(current.node[current.split] - looking[current.split])
        if pq.qsize() < maxsize or splitDistance < pq.queue[0].distance:
            child = current.l if current.l != None else current.r
            if child != None:
                current = search(child)
                print current.node, '***'
            else:
                insert(current)
        if current.f.l == current:
            current.f.l = None
        elif current.f.r == current:
            current.f.r = None
        current = current.f             
            
def insert(current):
    distance = cal(current.node, looking)
    if not pq.full():
        res = Res(distance, current)
        pq.put(res)
    elif pq.full() and distance < pq.queue[0].distance:
        res = Res(distance, current)
        pq.get()
        pq.put(res)

if __name__ == '__main__':
    root = buildKDTree(input, 0, None, 1)
    solve(root)
    while not pq.empty():
        haha = pq.get()
        print haha.node.node,haha.distance,'hahah'
        
        
        
#        print current.node
#        if current.flag == 1:
#            current = current.f
#            continue
#        current.flag = 1
#        distance = cal(current.node, looking)
#        print distance, pq.queue[0].distance,pq.queue[0].node.node,'distance'
#        if not pq.full() or distance < pq.queue[0].distance:
#            res = Res(distance, current)
#            if pq.full():
#                pq.get()
#            pq.put(res)
#        splitDistance = abs(current.node[current.split] - looking[current.split])
#        print splitDistance, pq.queue[0].distance,pq.queue[0].node.node
#        if splitDistance < pq.queue[0].distance or (not pq.full):
#            if current.l != None and current.l.flag == 1 and current.r != None and current.r.flag == 0:
#                current = current.r
#            elif current.r != None and current.r.flag == 1 and current.l != None and current.l.flag == 0:
#                current = current.l
#            else:
#                continue
#            if current != None:
#                print current.node , '****'
#                current = search(current)
#                distance = cal(current.node, looking)
#                res = Res(distance, current)
#                if not pq.full() or distance < pq.queue[0].distance:
#                    if pq.full():
#                        pq.get()
#                    pq.put(res)   