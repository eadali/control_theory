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
from pandas import DataFrame




# PENDULUM PARAMETERS
# =============================================================================
# Mass of pendulum [kg]
m = 1

# Length of pendulum [m]
l = 1

# Friction coeff of pendulum [N*s/m]
b = 0.25

# Gravity acceleration [m/s**2]
g = 9.8

# Initial state of pendulum = [angular position, angular veloctiy]
x_0 = [pi, 0]
# =============================================================================



# DISTURBANCE PARAMETERS
# =============================================================================
# Force value applied for disturbance [N]
dist_force = 8

# Time step that disturbance force applied
dist_timestep = 16
# =============================================================================



## CONTROLLER PARAMETERS
# =============================================================================
# Propotional gain value (optimization parameter)
k_p = 16

# Integral gain value (optimization parameter)
k_i = 0.01

# Derivative gain value (optimization parameter)
k_d = 16

# Reference position of pendulum
ref = pi
# =============================================================================



# SIMULATION PARAMETERS
# =============================================================================
num_timesteps = 256
# =============================================================================



# CREATE PID CONTROLLER AND INV PENDULUM MODEL
# =============================================================================
# Creates a PID controller
pid = pid_controller(k_p, k_i, k_d)
#pid = pid_controller(0, 0, 0)

# Creates a pendulum model
pendulum = pendulum_model(m, l, b, g, x_0)
# =============================================================================



# SIMULATE FEEDBACK SYSTEM
# =============================================================================

# Torque requested by PID controller(control signal)
u = 0

# History of inv pendulum angle
theta = list()

# History of requested torque
req_torque = list()

# Control cycle
for t in range(num_timesteps):
    # Apply requested torque and disturbance force to pendulum
    if t == dist_timestep:
        y = pendulum.update(u+dist_force*l)
    else:
        y = pendulum.update(u)

    # Calculate error of pendulum angle
    e = ref - y

    # Calculate requested torque by PID controller
    u = pid.update(e)

    # Add angle of pendulum to the history
    theta.append(y)

    # Add requested torque to the history
    req_torque.append(u)
# =============================================================================



# PRINT HISTORY TO TERMINAL AND TEXT FILE
# =============================================================================
history = dict()
history['timestep'] = list(range(num_timesteps))
history['requested_torque'] = req_torque
history['pendulum_angle'] = theta

history = DataFrame(history).to_string(index=False)

print(history)
with open('history.csv', 'w') as history_file:
    history_file.write(history)
# =============================================================================



# ANIMATE SIMULATION RESULT
# =============================================================================
pyplot.ion()
fig = pyplot.figure(figsize=(8, 8))

for t, y in enumerate(theta):
    pyplot.clf()

    # Animates inverted pendulum system
    x_pos = sin(y)
    y_pos = -cos(y)

    pyplot.subplot(2,2,1)
    pyplot.scatter([x_pos], [y_pos], s=256, marker='o', c='r', zorder=10)
    pyplot.scatter([0], [0], s=64, marker='+', c='r', zorder=10)
    pyplot.plot([0,x_pos], [0,y_pos])
    pyplot.xlim([-1.2,1.2])
    pyplot.ylim([-1.2,1.2])
    pyplot.tick_params(labelbottom=False, labelleft=False)
    pyplot.grid()

    # Plots angle position of pendulum
    pyplot.subplot(2,2,3)
    pyplot.xlim([0,len(theta)])
    pyplot.ylim([min(theta)-0.5, max(theta)+0.5])
    pyplot.plot(theta[:t], label='theta(t)')
    pyplot.xlabel('Time[s]')
    pyplot.ylabel('Pendulum Angle[radius]')
    pyplot.legend(loc='best')
    pyplot.grid()

    # Plots requested torque by PID controller
    pyplot.subplot(2,2,2)
    pyplot.xlim([0,len(req_torque)])
    pyplot.ylim([min(req_torque)-0.5, max(req_torque)+0.5])
    pyplot.plot(req_torque[:t], label='u(t)')
    pyplot.xlabel('Time[s]')
    pyplot.ylabel('Requested Torque[Nm]')
    pyplot.legend(loc='best')
    pyplot.grid()

    pyplot.tight_layout()
    pyplot.show()
    pyplot.pause(0.001)
# =============================================================================

    #fig.savefig('_tmp{:05d}.png'.format(time_index), bbox_inches='tight')