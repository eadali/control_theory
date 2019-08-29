#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 11:20:00 2019

@author: eadali
"""

from numpy import cos, linspace, pi, cumsum
from matplotlib import pyplot




class pid_controller:
    def __init__(self, k_p, k_i, k_d):
        """Inits PID contoller parameters

        # Arguments
            k_p: Proportional gain
            k_i: Integral gain
            k_d: Derivative gain
        """

        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d

        # First cycle check
        self.first = True

        # Integral value of PID
        self.i = 0

        # Previous value of error valeu
        self.e_m1 = 0


    def update(self, e):
        """Interface function for PID controller

        # Arguments
            e: error value

        # Returns
            control signal for model
        """

        # If first cycle, derivative and integral value equal to 0
        if self.first:
            # Calculates control signal
            u = self.k_p*e + self.k_i*0 + self.k_d*0
            self.first = False

        else:
            # Calculates derivative of error
            de = e - self.e_m1

            # Calculates control signal
            u = self.k_p*e + self.k_i*self.i + self.k_d*de

        # Calculates integral valeu of PID
        self.i = self.i + e

        # Saves error value for derivative calculation
        self.e_m1 = e

        return u




if __name__ == '__main__':
    """Test of pid_controller class
    """

    p_pid = pid_controller(k_p=1, k_i=0, k_d=0)
    i_pid = pid_controller(k_p=0, k_i=1/16, k_d=0)
    d_pid = pid_controller(k_p=0, k_i=0, k_d=8)
    e_signal = cos(linspace(0, 4*pi, 100))

    p_signal = list()
    i_signal = list()
    d_signal = list()

    for e in e_signal:
        p_signal.append(p_pid.update(e))
        i_signal.append(i_pid.update(e))
        d_signal.append(d_pid.update(e))

    pyplot.subplot(2,1,1)
    pyplot.plot(e_signal)

    pyplot.subplot(2,1,2)
    pyplot.plot(p_signal, 'b')
    pyplot.plot(i_signal, 'g')
    pyplot.plot(d_signal, 'r')
    pyplot.show()



