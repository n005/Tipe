import georinex as gr
import matplotlib.pyplot as plt

obs = gr.load('datatest2/nav.22n')
df = obs.to_dataframe()

print(df.columns.tolist())