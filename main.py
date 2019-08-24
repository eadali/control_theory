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

pid = pid_controller(5,0.001,6)
pendulum = pendulum_model(0.25, 5, [pi-0.4,0])
pendulum_2 = pendulum_model(0.25, 5, [pi-0.4,0])

r = pi
u = 0
theta = list()
test = list()
y_z = list()

for t in range(1000):
    y_z.append(pendulum_2.update(0))
    y = pendulum.update(u)
    e = r - y
    u = pid.update(e)
    test.append(u)

    theta.append(y)

#pyplot.ion(
#for y in theta:
#    pyplot.clf()
#    x = sin(y)
#    y = cos(y)
#    pyplot.plot([0,x],[0,y])
#    pyplot.show()
#    pyplot.pause(0.01)

pyplot.plot(theta, label='with_p')
pyplot.plot(y_z, label='thet')
pyplot.ylim([-4,4])
#
pyplot.legend(loc='best')
pyplot.xlabel('t')
pyplot.grid()
pyplot.show()



