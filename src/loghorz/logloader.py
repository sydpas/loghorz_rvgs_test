import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

plt.ion()

from welly import Well

import welly
print(welly.__version__)

ki_ret = Well.from_las(
                 "C:/Users/sydneyp/gitprojects/rvgs_2025_loghorz_test/las_files/HighResolution_full_SelCrv.LAS")
# may need to use LASIO to make LAS from v3.0 to v1.2 or v2.0


print(ki_ret)

print('Header:')
print(ki_ret.header)

print(ki_ret.location)

tracks = ['DT', 'GR', 'GRX', 'ILD', 'ILM', 'SFL', 'SP', 'RHOB', 'PE']
ki_ret.plot(tracks=tracks)

plt.show(block=True)








