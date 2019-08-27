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


external_force_value = 4
external_force_timestep = 16


# Creates a PID controller
pid = pid_controller(k_p=6, k_i=0.001, k_d=6)
#pid = pid_controller(k_p=0, k_i=0, k_d=0)

# Creates a pendulum model
pendulum = pendulum_model(0.25, 5, [pi,0])

# Reference value for tracking
r = pi


u = 0

# Inverted pendulum angle
theta = list()
control_signal = list()

# Control cycle
for t in range(256):
    # Apply input signal value
    if t == external_force_timestep:
        y = pendulum.update(u+external_force_value)
    else:
        y = pendulum.update(u)

    # Calculate error value
    e = r - y

    # Calculate input signal value
    u = pid.update(e)

    control_signal.append(u)
    theta.append(y)

# Animates inverted pendulum
pyplot.ion()
fig = pyplot.figure(figsize=(4, 8))

for time_index, y in enumerate(theta):
    pyplot.clf()

    x_pos = sin(y)
    y_pos = -cos(y)

    pyplot.subplot(2,1,1)
    pyplot.scatter([x_pos], [y_pos], s=256, marker='o', c='r', zorder=10)
    pyplot.scatter([0], [0], s=64, marker='+', c='r', zorder=10)
    pyplot.plot([0,x_pos], [0,y_pos])
    pyplot.xlim([-1.2,1.2])
    pyplot.ylim([-1.2,1.2])
    pyplot.grid()

    pyplot.subplot(2,1,2)
    pyplot.xlim([0,len(control_signal)])
    pyplot.ylim([min(control_signal)-0.5, max(control_signal)+0.5])
    pyplot.plot(control_signal[:time_index])
    pyplot.grid()
    #fig.savefig('_tmp{:05d}.png'.format(time_index), bbox_inches='tight')

    pyplot.show()
    pyplot.pause(0.00001)
