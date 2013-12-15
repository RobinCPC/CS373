# -*- coding: utf-8 -*-
"""
Created on Tue Dec 03 21:17:16 2013

@author: USER
"""

# In this exercise, try to write a program that
# will resample particles according to their weights.
# Particles with higher weights should be sampled
# more frequently (in proportion to their weight).

# Don't modify anything below. Please scroll to the 
# bottom to enter your code.

from math import *
import random

landmarks  = [[20.0, 20.0], [80.0, 80.0], [20.0, 80.0], [80.0, 20.0]]
world_size = 100.0

class robot:
    def __init__(self):
        self.x = random.random() * world_size
        self.y = random.random() * world_size
        self.orientation = random.random() * 2.0 * pi
        self.forward_noise = 0.0;
        self.turn_noise    = 0.0;
        self.sense_noise   = 0.0;
    
    def set(self, new_x, new_y, new_orientation):
        if new_x < 0 or new_x >= world_size:
            raise ValueError, 'X coordinate out of bound'
        if new_y < 0 or new_y >= world_size:
            raise ValueError, 'Y coordinate out of bound'
        if new_orientation < 0 or new_orientation >= 2 * pi:
            raise ValueError, 'Orientation must be in [0..2pi]'
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)
    
    
    def set_noise(self, new_f_noise, new_t_noise, new_s_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.forward_noise = float(new_f_noise);
        self.turn_noise    = float(new_t_noise);
        self.sense_noise   = float(new_s_noise);
    
    
    def sense(self):
        Z = []
        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            dist += random.gauss(0.0, self.sense_noise)
            Z.append(dist)
        return Z
    
    
    def move(self, turn, forward):
        if forward < 0:
            raise ValueError, 'Robot cant move backwards'         
        
        # turn, and add randomness to the turning command
        orientation = self.orientation + float(turn) + random.gauss(0.0, self.turn_noise)
        orientation %= 2 * pi
        
        # move, and add randomness to the motion command
        dist = float(forward) + random.gauss(0.0, self.forward_noise)
        x = self.x + (cos(orientation) * dist)
        y = self.y + (sin(orientation) * dist)
        x %= world_size    # cyclic truncate
        y %= world_size
        
        # set particle
        res = robot()
        res.set(x, y, orientation)
        res.set_noise(self.forward_noise, self.turn_noise, self.sense_noise)
        return res
    
    def Gaussian(self, mu, sigma, x):
        
        # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))
    
    
    def measurement_prob(self, measurement):
        
        # calculates how likely a measurement should be
        
        prob = 1.0;
        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            prob *= self.Gaussian(dist, self.sense_noise, measurement[i])
        return prob
    
    def __repr__(self):
        return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))



def eval(r, p):
    sum = 0.0;
    for i in range(len(p)): # calculate mean error
        dx = (p[i].x - r.x + (world_size/2.0)) % world_size - (world_size/2.0)
        dy = (p[i].y - r.y + (world_size/2.0)) % world_size - (world_size/2.0)
        err = sqrt(dx * dx + dy * dy)
        sum += err
    return sum / float(len(p))

#myrobot = robot()
#myrobot.set_noise(5.0, 0.1, 5.0)
#myrobot.set(30.0, 50.0, pi/2)
#myrobot = myrobot.move(-pi/2, 15.0)
#print myrobot.sense()
#myrobot = myrobot.move(-pi/2, 10.0)
#print myrobot.sense()

myrobot = robot()
myrobot = myrobot.move(0.1, 5.0)
Z = myrobot.sense()

N = 1000
p = []
for i in range(N):
    x = robot()
    x.set_noise(0.05, 0.05, 5.0)
    p.append(x)

p2 = []
for i in range(N):
    p2.append(p[i].move(0.1, 5.0))
p = p2

w = []
for i in range(N):
    w.append(p[i].measurement_prob(Z))


#### DON'T MODIFY ANYTHING ABOVE HERE! ENTER CODE BELOW ####
# You should make sure that p3 contains a list with particles
# resampled according to their weights.
# Also, DO NOT MODIFY p.

# current code is not good enough, for ponts whose weight over 0.1 will use 
# the same possiblility to resample them

p3 = []
sum_W = 0

# find summation of weight
for i in range(len(w)):
    sum_W += w[i]

print sum_W

# normalize weighting
count = 0
for i in range(len(w)):
    if (w[i] / sum_W < 0.001):
        w[i] = 0
    else:
        w[i] /= sum_W
        count +=1

print w
print count

#resample
# point in the range of weight from 0.1 to 0.01
for i in range(10):
    temp_p =[]
    temp_pInd = []
    for j in range(len(w)):
        if (w[j] < (0.1-i*0.01) and w[j] > (0.1-(i+1)*0.01)):
            temp_p.append(w[j])
            temp_pInd.append(j)
        # check how many w[j] in this probility range
    n_par = len(temp_p)
    n_sample = 0
    n_sample = int(sum(temp_p)*1000) #int((0.1-(i+1)*0.01)*1000)*n_par
    for j in range(n_sample):  # random pick in this range
        p3.append(p[random.choice(temp_pInd)])
        #cur_ind = temp_p
# point in the range over 0.1
if (len(p3) > 1000):
    p3 = p3[0:999]
else:
    temp_p =[]
    temp_pInd = []
    for j in range(len(w)):
        if (w[j] > (0.1)):
            temp_p.append(w[j])
            temp_pInd.append(j)
    n_sample = int(sum(temp_p)*1000)
    for j in range(n_sample):
        p3.append(p[random.choice(temp_pInd)])

# point in the range lower 0.01
if (len(p3) > 1000):
    p3 = p3[0:999]
else:
    temp_p =[]
    temp_pInd = []
    for j in range(len(w)):
        if (w[j] < (0.01)):
            if w[j]==0:
                test = 0
            else:
                temp_p.append(w[j])
                temp_pInd.append(j)
    n_sample = 1000 - len(p3) #int(sum(temp_p)*1000)
    for j in range(n_sample):
        p3.append(p[random.choice(temp_pInd)])
        #cur_ind = temp_p

p = p3