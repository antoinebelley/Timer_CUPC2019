import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from time import sleep

plt.axes()

circle = plt.Circle((0, 0), radius=0.75, fc='g')
plt.gca().add_patch(circle)
plt.axis('scaled')
plt.draw()





plt.pause(7*60)
plt.clf()
circle = plt.Circle((0, 0), radius=0.75, fc='y')
plt.gca().add_patch(circle)
plt.axis('scaled')
plt.pause(3)
plt.clf()
circle = plt.Circle((0, 0), radius=0.75, fc='r')
plt.gca().add_patch(circle)
plt.axis('scaled')
plt.pause(1*60)
