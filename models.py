#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 22:36:20 2019

@author: eadali
"""

from scipy.integrate import odeint
from numpy import sin
from matplotlib import pyplot




class pendulum_model:
    def __init__(self, m, l, b, g, x_0):
        """Inits pendulum constants and initial state

        # Arguments
            m: Pendulum mass
            l: Pendulum length
            b: Pendulum friction coeff
            g: Earth gravity acceleration
            x_0: Pendulum initial state
        """

        self.m = m
        self.l = l
        self.b = b
        self.g = g

        self.x_0 = x_0



    def ode(self, x, t, u):
        """Dynamic equations of pendulum

        # Arguments
            x: [angle of pendulum, angular velocity of pendulum]
            t: Time steps for ode solving
            u: External force applied to the pendulum

        # Returns
            Derivative of internal states
        """

        # Calculates equation coeffs
        c_1 = -self.b/(self.m*self.l**2)
        c_2 = -self.g/self.l
        c_3 = 1.0/(self.m*self.l**2)

        # ODE of pendulum
        theta, omega = x
        dxdt = [omega, c_1*omega + c_2*sin(theta) + c_3*u]

        return dxdt



    def update(self, u):
        """Interface function for pendulum model

        # Arguments
            u: External force applied to the pendulum

        # Returns
            Angle of pendulum
        """

        # Solving ODE with scipy library
        x = odeint(self.ode, self.x_0, [0,0.1], args=(u,))

        self.x_0 = x[1]

        return x[1,0]



if __name__ == '__main__':
    """Test of pendulum_model class
    """
    pendulum = pendulum_model(1, 1, 0.25, 9.8, [1,0])
    theta = list()

    for t in range(512):
        theta.append(pendulum.update(0.4))

    pyplot.plot(theta, label='theta(t)')
    pyplot.legend(loc='best')
    pyplot.xlabel('t')
    pyplot.grid()
    pyplot.show()