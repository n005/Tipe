# -*- coding: utf-8 -*-

import georinex as gr
import matplotlib.pyplot as plt
import numpy as np

obs = gr.load('rinex.22o')
df = obs.to_dataframe()
ecef = obs.position

Satnb="G30"

df = df.reset_index()
print(df.columns.tolist())
val = df[df['sv'].isin([Satnb])]

deltaSR = val["C1C"]-val["C5Q"]
#deltaSR = np.sqrt(val["C1C"]**2+val["C5X"]**2)

plt.plot(val.time, deltaSR)

table = plt.table(cellText=[[int(np.mean(deltaSR)), int(np.std(deltaSR)),
                                 int(np.min(deltaSR)), int(np.max(deltaSR))]],
                      rowLabels=["Value"],
                      colLabels=["Mean", "Std", "Min", "Max"],
                      loc='bottom', bbox=[0, -0.3, 1, 0.1])

plt.title("Delta speudo-range sat. " + Satnb + " between L1 & L5 bands")
plt.xlabel("Time")
plt.ylabel("Delta speudo-range")
plt.show()