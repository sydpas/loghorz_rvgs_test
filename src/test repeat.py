from andy.andy12_repeat import (andy12)

# call necessary bg functions
_, non_depth_curves, _, _ = andy12()

# just for knowing the index of all curves
for i, curve in enumerate(non_depth_curves, start=0):
    print(f'{i}: {curve}')

# using the non_depth_curves list, we can group accordingly...
ax1 = [non_depth_curves[1], non_depth_curves[5]]
col1 = len(ax1)
ax2 = [non_depth_curves[2]]
col2 = len(ax2)
ax3 = [non_depth_curves[1]]
col3 = len(ax3)
ax4 = [non_depth_curves[7], non_depth_curves[6], non_depth_curves[1]]
col4 = len(ax4)
ax5 = [non_depth_curves[0]]
col5 = len(ax5)


ax_list = [ax1, ax2, ax3, ax4, ax5]
col_list = [col1, col2, col3, col4, col5]

