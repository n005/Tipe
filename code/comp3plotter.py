# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

colnames=['TIME', 'PRN', 'misure'] 
df = pd.read_csv('C:/Users/n005/Documents/TIPE/data/datatest/t.txt', names=colnames, header=None)

val = df[df['PRN'] != 1006]

plt.scatter(val['TIME'], val['misure'])
plt.title("Multipath error")
plt.xlabel("Time (s)")
plt.ylabel("Error (m)")
