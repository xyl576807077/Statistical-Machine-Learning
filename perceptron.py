# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 21:12:48 2016

@author: Administrator
"""

import copy

training_set = [[(3, 3), 1], [(10, 3), 1], [(-10, -2), -1], [(-5, 0), -1]]
w = [0, 0]
b = 0
history = []
learning_rate = 1
iter = 0

def check():
    flag = False
    for i in range(len(training_set)):
        x = training_set[i][0]
        y = training_set[i][1]
        if cal(x, y) <= 0:
            update(x, y)
            flag = True
    if not flag:
        print w, b
    return flag                
        
def cal(x, y):
    res = 0
    for i in range(len(x)):
        res += x[i] * w[i]
    res += b
    res *= y
    return res
    
def update(x, y):
    global w, b, history, iter
    iter += 1
    for i in range(len(x)):
        w[i] += x[i] * (y * learning_rate)
    b += learning_rate * y
    history.append([copy.copy(w), b])
    
if __name__ == "__main__":
    for i in range(1000):
        if not check(): 
            print iter            
            break
    