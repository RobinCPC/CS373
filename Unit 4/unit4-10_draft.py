# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:33:58 2013

@author: USER
"""

# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. NOTE: the 'v' should be 
# lowercase.
#
# Your function should be able to do this for any
# provided grid, not just the sample grid below.
# ----------


# Sample Test case
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# ----------------------------------------
# modify code below
# ----------------------------------------

def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    #add an array called expand
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    e_step = 0
    expand[init[0]][init[1]] = e_step
    
    #add an array for g_value
    #g_val = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    #add array called shortest
    shortest = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    start = False   # flag that is set when shortest path found (back to init)    

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complet
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                found = True
                print next
                # find shortest path
                shortest[goal[0]][goal[1]] = '*'
                prev = [expand[x][y], x, y]     # find previos grid back to origin
                while not start:
                    for i in range(len(delta)):
                        px = prev[1] - delta[i][0]
                        py = prev[2] - delta[i][1]
                        if px >= 0 and px < len(grid) and py >= 0 and py < len(grid[0]):
                            if expand[px][py] < prev[0] and expand[px][py] != -1:
                                shortest[px][py] = delta_name[i]    # update shortest path
                                prev =[expand[px][py], px, py]
                                if px == init[0] and py == init[1]:
                                    start = True
                                break
                                
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            # add expand
                            e_step += 1
                            expand[x2][y2] = e_step
                            #add g_value
                            #g_val[x2][y2] = g2
    print
    for i in range(len(expand)):
        print expand[i]
    print
    for i in range(len(closed)):
        print closed[i]
    print
    for i in range(len(shortest)):
        print shortest[i]
    return shortest # make sure you return the shortest path.

search()