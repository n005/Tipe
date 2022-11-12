# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd

data = np.genfromtxt('datatest2/output.txt', delimiter=',')

data2 = np.loadtxt('datatest2/output.txt', delimiter=',', usecols=[3,5])
time = np.loadtxt('datatest2/output.txt', delimiter=',',dtype=np.int64, usecols=[0])

lat=data[:, 3]
lon=data[:, 5]
#time=data[:,0]
time = pd.to_datetime(time/1000, origin='unix', unit='s')

#plt.plot(lat, lon, '+')
plt.show()
#z=range(len(lat))

f, ax = plt.subplots()
points=ax.scatter(lon, lat, c=time)
f.colorbar(points, label="Time")
ax.set_title("Position")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
plt.show()

RSD=np.sqrt(lat**2+lon**2)
plt.plot(time, RSD)
plt.title("Root Squared Distance")
plt.xlabel("Time")
plt.ylabel("RSD")
plt.show()

'''
dRSD=np.diff(RSD)
plt.plot(time[1:], dRSD)
plt.title("Derivative of Root Squared Distance")
plt.xlabel("Time")
plt.ylabel("dRSD")
plt.show()
'''