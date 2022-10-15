import georinex as gr
import matplotlib.pyplot as plt

obs = gr.load('rinex.22o')
df = obs.to_dataframe()

L1freq=1575.42
L5freq=1176.45

def TEC(f1,f5,L1,L5):
    K=40.308e16
    c=299792458
    g1=c/f1
    g5=c/f5
    return (1/K)*((f1**2*f5**2)/(f1**2-f5**2))*(L1*g1-L5*g5)


ecef = obs.position
df = df.reset_index()
print(df.columns.tolist())
val = df[df['sv'].isin(['G30'])]

TECtab=TEC(L1freq, L5freq, val["L1C"], val["L5Q"])

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_title("L1 Band sat. G30")
ax1.set_xlabel('time')
ax1.set_ylabel('phase', color=color)
ax1.plot(val.time, val["L1C"], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Signal Strength (dBhz)', color=color)
ax2.plot(val.time, val["S1C"], color=color)
ax2.tick_params(axis='y', labelcolor=color)
#plt.plot(df.index, df["L1C"])

fig.tight_layout()
plt.show()

fig, bx1 = plt.subplots()

color = 'tab:red'
bx1.set_title("L5 Band sat. G30")
bx1.set_xlabel('time')
bx1.set_ylabel('phase', color=color)
bx1.plot(val.time, val["L5Q"], color=color)
bx1.tick_params(axis='y', labelcolor=color)

bx2 = bx1.twinx()

color = 'tab:blue'
bx2.set_ylabel('Signal Strength (dbHZ)', color=color)
bx2.plot(val.time, val["S5Q"], color=color)
bx2.tick_params(axis='y', labelcolor=color)
#plt.plot(df.index, df["L1C"])

fig.tight_layout()
plt.show()

fig, cx1 = plt.subplots()

color = 'tab:blue'
cx1.set_title("TEC sat. G30")
cx1.set_xlabel('time')
cx1.set_ylabel('sTEC, TECU', color=color)
cx1.plot(val.time, TECtab, color=color)
cx1.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()