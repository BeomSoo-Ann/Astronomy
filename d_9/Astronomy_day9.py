import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

dt= 1
A_position= np.array([0,0,0], dtype='f')
B_position= np.array([150,0,0], dtype='f')

A_velocity= np.array([0,0,0], dtype='f')
B_velocity= np.array([0,-5,0], dtype='f')

A_mass= 5000
B_mass= 500

step= 1000

def gravity(position1, position2, mass1, mass2):
    G=1
    distance= np.sqrt(np.sum((position2-position1)**(2)))

    direction= (position2-position1)/distance

    force= G*((mass1*mass2)/(distance**2))*direction
    
    return force

fig= plt.figure()

for i in range(step):

    A_accel= (1/A_mass)*gravity(A_position, B_position, A_mass, B_mass)
    B_accel= (1/B_mass)*gravity(B_position, A_position, B_mass, A_mass)

    A_position= A_position + A_velocity*dt + (1/2)*A_accel*(dt**2)
    B_position= B_position + B_velocity*dt + (1/2)*B_accel*(dt**2)

    A_velocity= A_velocity + A_accel*dt
    B_velocity= B_velocity + B_accel*dt

    ax= plt.axes(projection='3d')

    ax.scatter(A_position[0], A_position[1], A_position[2], color='r', marker='o', s=150)
    ax.scatter(B_position[0], B_position[1], B_position[2], color='b', marker='o', s=50)

    ax.set_xlim(-150,150)
    ax.set_ylim(-150,150)
    ax.set_zlim(-150,150)

    plt.pause(0.01)
    plt.clf()
