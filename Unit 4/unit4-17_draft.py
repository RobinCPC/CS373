# -*- coding: utf-8 -*-
"""
Created on Sun Mar 02 21:31:14 2014

@author: USER
"""

# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------

def compute_value():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[goal[0]][goal[1]] = 1
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    
    x = goal[0]
    y = goal[1]
    v = 0
    #value[x][y] = v

    open = [[v, x, y]]    
    
    over = False    # flag that is set when computing over
    resign = False  # flag set if algorithn can't compute all 

    while not over and not resign:
        if len(open) == 0:
            over = True
            #return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            v = next[0]
            value[x][y] = v
            
            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]
                
                if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                    if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                        v2 = v + cost_step
                        open.append([v2, x2, y2])
                        closed[x2][y2] = 1
    for i in range(len(value)):
        print value[i]
    return value #make sure your function returns a grid of values as demonstrated in the previous video.

compute_value()

