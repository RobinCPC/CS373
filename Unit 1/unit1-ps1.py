# -*- coding: utf-8 -*-
"""
Created on Sun Nov 03 22:14:53 2013

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

p = [[0.05,0.05,0.05,0.05,0.05],
     [0.05,0.05,0.05,0.05,0.05],
     [0.05,0.05,0.05,0.05,0.05],
     [0.05,0.05,0.05,0.05,0.05]]  # may need a function to declare 

#p = [[1./9,1./9,1./9],[1./9,1./9,1./9],[1./9,1./9,1./9]]

def sense2D(p,Z):
    q = []
    norm = 0.    # normalization factor of probability
    for i in range(len(colors)):
        q.append([])    #initial a empty column in firs row
        for j in range(len(colors[i])):
            hit = (Z == colors[i][j])
            q[i].append(p[i][j]*(hit * sensor_right + (1-hit) * (1-sensor_right)))
        norm = norm + sum(q[i])
    for i in range(len(colors)):
        for j in range(len(colors[i])):
            q[i][j] /= norm
    return q
    
def move2D(p,U):
    q = []
    for i in range(len(colors)):
        q.append([])   #initial a empty column in firs row
        for j in range(len(colors[i])):
            if U[0] == 0 and U[1] == 0: # no move
                q[i].append(p[i][j])    # same as before
            elif U[1] == 0:   # move vertical (row)
                s = p_move * p[(i-U[0]) % len(colors)][j]
#                s = s + ((1-p_move)/2) * p[(i-U[0]-1) % len(colors)][j]
#                s = s + ((1-p_move)/2) * p[(i-U[0]+1) % len(colors)][j]
                s = s + (1-p_move) * p[i][j]
                q[i].append(s)
            else:
                s = p_move * p[i][(j-U[1]) % len(colors[0])]
#                s = s + ((1-p_move)/2) * p[i][(j-U[1]-1) % len(colors[0])]
#                s = s + ((1-p_move)/2) * p[i][(j-U[1]+1) % len(colors[0])]
                s = s + (1-p_move) * p[i][j]
                q[i].append(s)
    return q

for i in range(len(motions)):
    p = move2D(p, motions[i])
    p = sense2D(p,measurements[i])
#Your probability array must be printed 
#with the following code.

show(p)





