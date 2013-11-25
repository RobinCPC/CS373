# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 21:10:04 2013

@author: USER
"""

#Modify the program to find and print the sum of all 
#the entries in the list p.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
pHit = 0.6
pMiss = 0.2

p[0]=p[0]*pMiss
p[1]=p[1]*pHit
p[2]=p[2]*pHit
p[3]=p[3]*pMiss
p[4]=p[4]*pMiss

summ = 0.
n=5

for i in range(0,n):
    summ += p[i]

for i in range(0,n):
    p[i] /= summ


print p