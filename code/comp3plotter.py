# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from COMPACT3 import compread
import numpy as np
import pandas as pd
from scipy.stats import norm

val=compread('C:/Users/n005/Documents/TIPE/data/datatest/obs.m15')
val = val[val['PRN'] != 'G06']

misure=pd.to_numeric(val['misure'], errors='coerce')

mu, std = norm.fit(misure.dropna()) 

plt.scatter(val['TIME'], misure)
plt.title("Multipath error")
plt.xlabel("Time")
plt.ylabel("Error (m)")
plt.show()

misure.plot(kind='hist', title="Multipath distribution", density=True, grid=True)
plt.xlabel("Multipath distance (m)")
plt.suptitle("Multipath distribution", y=1.05, fontsize=16)

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
  
plt.plot(x, p, 'k', linewidth=2)
title = "Fit Values: μ: {:.2f} and σ: {:.2f}".format(mu, std)
plt.title(title, fontsize=12)
plt.show()
