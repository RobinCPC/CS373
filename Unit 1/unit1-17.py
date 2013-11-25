# -*- coding: utf-8 -*-
"""
Created on Sun Nov 03 02:10:21 2013

@author: USER
"""

#Program a function that returns a new distribution 
#q, shifted to the right by U units. If U=0, q should 
#be the same as p.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    #
    #ADD CODE HERE
    q = []
    for i in range(len(p)):
        q.append(p[i])
    
    if U == 0 or (U % len(p)) == 0:
        return q
    else:
        if U > len(p):
            U %= len(p)
        for i in range(len(p)):
            print i-U
            print [(i-U) % len(p)]
            if i+U > len(p)-1:
                q[i+U-len(p)] = p[i]
            else:
                q[i+U] = p[i]
    #
    return q

print move(p, 2)