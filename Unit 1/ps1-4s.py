# -*- coding: utf-8 -*-
"""
Created on Mon Nov 04 00:57:02 2013

@author: USER
"""

colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

#colors = [['green', 'green', 'green'],
#          ['green', 'red', 'red'],
#          ['green', 'green', 'green']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

if len(measurements) != len(motions):
    raise ValueError, "error in size of measurements/motions vector"

pinit = 1 / float(len(colors)) / float(len(colors[0]))
p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]

def sense(p, colors, measurements):
    aux = [[0.0 for row in range(len(colors[0]))] for col in range(len(colors))]
    s = 0.0
    for i in range(len(colors)):
        for j in range(len(colors[i])):
            hit = (measurements == colors[i][j])
            aux[i][j] = p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right))
            s += aux[i][j]
    for i in range(len(colors)):
        for j in range(len(colors[i])):
            aux[i][j] /= s
    return aux

def move(p, motion):
    aux = [[0.0 for row in range(len(colors[0]))] for col in range(len(colors))]
    
    for i in range(len(colors)):
        for j in range(len(colors[i])):
            aux[i][j] = (p_move * p[(i-motion[0]) % len(p)][(j-motion[1]) % len(colors[i])] + (1-p_move)* p[i][j])
    return aux

for i in range(len(motions)):
    p = move(p, motions[i])
    p = sense(p, colors, measurements[i])
#Your probability array must be printed 
#with the following code.

show(p)