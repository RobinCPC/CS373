# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 16:40:48 2013

@author: USER
"""

# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def move_step(cur, way):    # get four posistion future posstion
    moved = []
    for n in way:
        moved.append([cur[0]+n[0], cur[1]+n[1]])
    return moved

def if_avil(way, grid):
    # remove way with minus element or on obstacle of grid
    new_way = []
    for i in range(len(way)):
        if (way[i][0] > -1 and way[i][0] < len(grid)) and (way[i][1] > -1 and way[i][1] < len(grid[0])):
            if (grid[way[i][0]][way[i][1]] != 1):
                new_way.append(way[i])    
    return new_way

def if_check(way,ch):
    # find if way is already checked
    new_way = []
    for i in range(len(way)):
        if way[i] not in ch:
            ch.append(way[i])
            new_way.append(way[i])
    return new_way, ch

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    init_v = [0, init[0], init[1]]      # initial  postion with zero cost
    # put initial position in checked postion list
    checked = []
    checked.append(init)    
    path = []   # initial path
    path.append(init_v)  # put initial and  cost
    found = False
    resign = False
    while found == False and resign == False:
        # check if arrived goal first
        for e in path:
            if e[1]==goal[0] and e[2]==goal[1]:
                path = e
                found = True
        # start search, find the element in path with lowest cost (sort)
        if (found == False):
            path.sort()
            sel_pos = path.pop(0)
            possible_way = move_step(sel_pos[1:], delta)
            possible_way = if_avil(possible_way, grid)
            possible_way, checked = if_check(possible_way, checked)
            # check if go to dead end
            if len(possible_way)==0 and len(path) ==0:
                path = 'fail'
                resign = True
            # import possible way with new cost
            for e in possible_way:
                path.append([sel_pos[0]+1, e[0], e[1]])
    return path # you should RETURN your result

print search()