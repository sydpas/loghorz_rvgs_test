import numpy as np

import matplotlib.pyplot as plt

from welly import Well

import welly
print(welly.__version__)

ki_ret = Well.from_las(
                 r"C:\Users\sydne\git\xrvgs\loghorz_rvgs_test\las_files\HighResolution_full_SelCrv.LAS")
# may need to use LASIO to make LAS from v3.0 to v1.2 or v2.0


print(ki_ret)

print('Header:')
print(ki_ret.header)

print(ki_ret.location)

tracks = ['DT', 'GR', 'GRX', 'ILD', 'ILM', 'SFL', 'SP', 'RHOB', 'PE']
ki_ret.plot(tracks=tracks)

plt.show(block=True)








