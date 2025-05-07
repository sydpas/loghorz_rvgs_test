import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from welly import Well

highres = Well.from_las("../../las_files/HighResolution_full_SelCrv.LAS")

print(highres.header)

curve_list = highres.data
columns = len(curve_list)

fig, ax = plt.subplots(figsize=(columns,6))

ax1 = plt.subplot2grid((1,5), (0,0), rowspan=1, colspan=1)
ax2 = plt.subplot2grid((1,5), (0,1), rowspan=1, colspan=1)
ax3 = plt.subplot2grid((1,5), (0,2), rowspan=1, colspan=1)
ax4 = plt.subplot2grid((1,5), (0,3), rowspan=1, colspan=1)
ax5 = ax3.twiny()  # puts curves together (like density/neutron)

# gamma ray curve
ax1.plot('GR', data=highres, color="red", linewidth = 0.5)
ax1.set_xlabel("Gamma")
ax1.set_ylabel("Depth (m)")
ax1.tick_params(axis='x', rotation=0)
ax1.title.set_color('red')

plt.tight_layout()
plt.show()
