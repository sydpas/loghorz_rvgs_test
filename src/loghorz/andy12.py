import pandas as pd
import matplotlib.pyplot as plt
import lasio
import numpy as np

las = lasio.read("../../las_files/HighResolution_full_SelCrv.LAS")

df = las.df()
df['DEPTH'] = df.index
print(df.describe())

df.plot(x='GR', y='DEPTH', color='black', linewidth=0.5, legend=False, figsize=(4,8))
plt.fill_betweenx(df['DEPTH'], df['GR'], 75, facecolor='yellow')
plt.fill_betweenx(df['DEPTH'], df['GR'], 0, facecolor='white')
plt.axvline(75, color='black', linewidth=0.5, alpha=0.5)
plt.title('Filled Gamma Curve')
plt.savefig('../../figures/filled_gamma_curve.png')
plt.show()

