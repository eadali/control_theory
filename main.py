#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 11:29:04 2019

@author: eadali
"""

from controllers import pid_controller
from models import pendulum_model
from matplotlib import pyplot
from numpy import sin, cos, pi



# Creates a PID controller
pid = pid_controller(k_p=6, k_i=0.001, k_d=6)
#pid = pid_controller(k_p=0, k_i=0, k_d=0)

# Creates a pendulum model
pendulum = pendulum_model(0.25, 5, [pi-0.8,0])

# Reference value for tracking
r = pi


u = 0

# Inverted pendulum angle
theta = list()

#
for t in range(128):
    # Apply input signal value
    y = pendulum.update(u)

    # Calculate error value
    e = r - y

    # Calculate input signal value
    u = pid.update(e)

    theta.append(y)

# Animates inverted pendulum
pyplot.ion()
pyplot.figure(figsize=(8, 8))

for y in theta:
    pyplot.clf()

    x_pos = sin(y)
    y_pos = -cos(y)

    pyplot.scatter([x_pos], [y_pos], s=256, marker='o', c='r', zorder=10)
    pyplot.scatter([0], [0], s=64, marker='+', c='r', zorder=10)
    pyplot.plot([0,x_pos], [0,y_pos])
    pyplot.xlim([-1.2,1.2])
    pyplot.ylim([-1.2,1.2])
    pyplot.grid()

    pyplot.show()
    pyplot.pause(0.001)