import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # TkAgg is a backend that determines how plots r displayed
import matplotlib.pyplot as plt
from welly import Well

ki_ret = Well.from_las(
                 r"C:\Users\sydne\git\rvgs\loghorz_rvgs_test\las_files\HighResolution_full_SelCrv.LAS")

print(ki_ret)
print('Header:')
print(ki_ret.header)
print(ki_ret.location)

curve_list = ['DT', 'GR', 'GRX', 'ILD', 'ILM', 'SFL', 'SP', 'RHOB', 'PE']
columns = len(curve_list)

# now we plot...
fig, axes = plt.subplots(1, columns, figsize=(columns * 1.5, 7))

colours = ['blue', 'black']
# pick specific colours for each curve

for i, curve in enumerate(curve_list):
    ax = axes[i]
    # plot ith curve
    ki_ret.data[curve].plot(
        ax, linestyle='-', linewidth=1, color=f'C{i}', marker='o', markersize=1, alpha=0.3)
    ax.set_title(f'{curve} Log', fontsize = 12, fontweight='bold')
    ax.grid(True, linestyle='-', alpha=0.3, linewidth=0.5)
    ax.tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.savefig("ki_ret_plot.png")
plt.show()








