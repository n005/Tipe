from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from matplotlib.widgets import Slider, Button

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

def plot3d_wthsat(*kepler):
    x = np.linspace(-5*np.pi, 5*np.pi, 500)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([0], [0], [0], color="g", s=100)
    for i in kepler:
        tmp = cartesian_3d(i[0], x)
        ax.plot(tmp[0], tmp[1], tmp[2], linewidth=0.5)
        tmp2 = cartesian_3d(i[0], i[1])
        ax.scatter(tmp2[0], tmp2[1], tmp2[2], s=70)
    plt.show()
    
    

def cursor():  
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    axa = plt.axes([0.25, 0.15, 0.65, 0.03])
    axe = plt.axes([0.25, 0.1, 0.65, 0.03])
    axi = plt.axes([0.25, 0.2, 0.65, 0.03])
    axomega = plt.axes([0.25, 0.25, 0.65, 0.03])
    axpomega = plt.axes([0.25, 0.30, 0.65, 0.03])
    axsat = plt.axes([0.25, 0.35, 0.65, 0.03])
    
    aax = Slider(axa, 'Semimajor Axis', 35000000, 37000000, 36000000)
    eax = Slider(axe, 'Eccentricity', 0.0, 1, 0)
    iax = Slider(axi, 'Inclination', 0.0, 2*np.pi, 0)
    omegaax = Slider(axomega, 'Longitude of the ascending node', 0.0, 2*np.pi, 0)
    pomegaax = Slider(axpomega, 'Argument of periapsis', 0.0, 2*np.pi, 0)
    satax = Slider(axsat, 'Eccentric anomaly', 0.0, 2*np.pi, 0)
    
    x = np.linspace(-5*np.pi, 5*np.pi, 500)
    ax.scatter([0], [0], [0], color="g", s=100)
    tmp = cartesian_3d(Kepler(36000000,0,0,0,0), x)
    l = ax.plot(tmp[0], tmp[1], tmp[2], linewidth=0.5)
    tmp22 = cartesian_3d(Kepler(36000000,0,0,0,0), 0)
    ax.scatter(tmp22[0], tmp22[1], tmp22[2], s=70)
    ax.set_xlim3d(-3e7, 3e7)
    ax.set_ylim3d(-3e7, 3e7)
    ax.set_zlim3d(-3e7, 3e7)
    
    def cursor_update(val):
        a = aax.val
        e = eax.val
        i = iax.val
        omega = omegaax.val
        pomega = pomegaax.val
        sat = satax.val
        tmp2 = cartesian_3d(Kepler(a,e,i,omega,pomega), x)
        tmp3 = cartesian_3d(Kepler(a,e,i,omega,pomega), sat)
        ax.clear()
        ax.plot(tmp2[0], tmp2[1], tmp2[2], linewidth=0.5)
        ax.scatter([0], [0], [0], color="g", s=100)
        ax.scatter(tmp3[0], tmp3[1], tmp3[2], s=70)
        ax.set_xlim3d(-3e7, 3e7)
        ax.set_ylim3d(-3e7, 3e7)
        ax.set_zlim3d(-3e7, 3e7)
    
    aax.on_changed(cursor_update)
    eax.on_changed(cursor_update)
    iax.on_changed(cursor_update)
    omegaax.on_changed(cursor_update)
    pomegaax.on_changed(cursor_update)
    satax.on_changed(cursor_update)

#cursor()
    

a=5153.68**2
e=0.00595074
i=0.93589
omega=-2.6631
pomega=2.75303

plot3d_wthsat([Kepler(a,e,i,omega,pomega), -np.pi/2])