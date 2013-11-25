# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 21:25:15 2013

@author: USER
"""

#Modify the code below so that the function sense, which 
#takes p and Z as inputs, will output the NON-normalized 
#probability distribution, q, after multiplying the entries 
#in p by pHit or pMiss according to the color in the 
#corresponding cell in world.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2


def sense(p, Z):
    #
    #ADD YOUR CODE HERE
    q =[]
    for i in range(0,len(p)):
        if world[i] == Z:
            q.append(p[i]*pHit)
        else:
            q.append(p[i]*pMiss)
        #hit = (world[i] == Z)
        #q.append(p[i] * (pHit*hit + pMiss*(1-hit)))
    norm = sum(q)
    for i in range(len(p)):
        q[i] /= norm
	#
    return q

print sense(p,Z)