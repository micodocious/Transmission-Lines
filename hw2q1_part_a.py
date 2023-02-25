# A sinusoidal wave f(z, t) = A sin(ωt + βz − π/6) with phase constant β = 0.4π rad/m travels with phase velocity vp 
# = 15 cm/ns. Determine (a) the direction of wave propagation, (b) the frequency of the wave, and (c) the wavelength 
# of the wave.

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
# References
# https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c
# https://riptutorial.com/matplotlib/example/23558/basic-animation-with-funcanimation
 
def func(t, line):
    t = np.arange(0,t,0.1)
    A = 1
    w = 2*np.pi
    b = 0.4*np.pi
    y = A*np.sin(-t)
    line.set_data(t, y)
    return line
 
fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(-1.2, 1.22))
redDots = plt.plot([], [], 'ro')
line = plt.plot([], [], lw=2)
 
# Creating the Animation object
line_ani = animation.FuncAnimation(fig, func, frames=np.arange(1,100,0.1), fargs=(line), interval=100, blit=False)
#line_ani.save(r'Animation.mp4')
 
 
plt.show()
