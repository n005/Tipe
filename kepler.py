from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

@dataclass
class Kepler:
    a: float
    e: float
    i: float
    omega: float
    pomega: float
    
def satpos(kepler, E):
    xhi = kepler.a*(np.cos(E)-kepler.e)
    eta = kepler.a*np.sqrt(1-kepler.e**2)*np.sin(E)
    zeta = 0
    return (xhi, eta, zeta)

def mean_motion (kepler):
    mu = 3.986005
    a = kepler.a
    return np.sqrt((mu/a)**3)

def mean_anomaly(kepler, t, t0):
    n=mean_motion(kepler)
    t=t-t0
    return n*t

def eccentric_anomaly(kepler, n):
    e= kepler.e
    return n+(e*np.sin(n))

def true_anomaly(kepler, E):
    e = kepler.e
    beta = e/(1+np.sqrt(1-e**2))
    return E+2*np.arctan((beta*np.sin(E))/(1-beta*np.cos(E)))

def r_norm(kepler, E):
    e=kepler.e
    return kepler.a*(1-(e*np.cos(E)))

def cartesian(kepler, E):
    r = r_norm(kepler,E)
    f = true_anomaly(kepler, E)
    x = r*np.cos(f)
    y = r*np.sin(f)
    z = 0
    return [x,y,z]

def R3(ang):
    return np.array([[np.cos(ang), np.sin(ang), 0],
                     [-np.sin(ang), np.cos(ang), 0],
                     [0, 0 ,1] ])

def R1(ang):
    return np.array([[1, 0, 0],
                     [0, np.cos(ang), np.sin(ang)],
                     [0, -np.sin(ang) , np.cos(ang)] ])

def cartesian_3d(kepler, x):
    tarray = np.matmul(np.matmul(np.matmul(R3(-kepler.omega), R1(-kepler.i)), R3(-kepler.pomega)),cartesian(kepler, x))
    return tarray

def plot3d(*kepler):
    x = np.linspace(-5*np.pi, 5*np.pi, 500)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([0], [0], [0], color="g", s=100)
    for i in kepler:
        tmp = cartesian_3d(i, x)
        ax.plot(tmp[0], tmp[1], tmp[2])
    plt.show()

a=36000000
e=0
i=0
omega=0
pomega=0

plot3d(Kepler(a,e,i,omega,pomega), Kepler(a,e,0.2,omega,pomega))
