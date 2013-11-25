# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 20:33:17 2013

@author: USER
"""

#Write a code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

#Enter code here
n = 5
for i in range(0,n):
    if i == 1 or i== 2:
        p[i] *=0.6
    else:
        p[i] *= 0.2
    p[i] = round(p[i],2)
    

print p