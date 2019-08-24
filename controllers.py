#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 11:20:00 2019

@author: eadali
"""

class pid_controller:
    def __init__(self, k_p, k_d, k_i):
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d

        self.first = True
        self.i = 0
        self.e_m1 = 0


    def update(self, e):
        if self.first:
            u = self.k_p*e + self.k_i*self.i + self.k_d*0
            self.first = False

        else:
            de = e - self.e_m1
            u = self.k_p*e + self.k_i*self.i + self.k_d*de

        self.i = self.i + e
        self.e_m1 = e

        return u
