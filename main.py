#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 11:29:04 2019

@author: eadali
"""

from controllers import pid_controller
from models import pendulum_model
from matplotlib import pyplot

pid = pid_controller(-2,-2,0)
pendulum = pendulum_model(0.25, 5, [1,0])

r = 0
u = 0
theta = list()
test = list()
for t in range(1000):
    y = pendulum.update(u)
    e = r - y
    u = pid.update(e)
    test.append(u)

    theta.append(y)

pyplot.plot(theta, label='theta(t)')
pyplot.plot(test, label='thet')

pyplot.legend(loc='best')
pyplot.xlabel('t')
pyplot.grid()
pyplot.show()



