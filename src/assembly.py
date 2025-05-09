from andy.andy12 import (andy12)

def organize_curves():
    """
    This function organizes curves and groups them together for plotting.

    Return:
        ax_list: list of all groups of curves.
    """

    # call necessary bg functions
    columns, non_depth_curves, curve_unit_list, df = andy12()

    for i, curve in enumerate(non_depth_curves, start=0):
        print(f'{i}: {curve}')

    # using the non_depth_curves list, we can group accordingly...
    ax1 = [non_depth_curves[1], non_depth_curves[6]]
    print(f'ax1: {ax1}')
    ax2 = [non_depth_curves[3]]
    print(f'ax1: {ax2}')
    ax3 = [non_depth_curves[1]]
    print(f'ax1: {ax3}')
    ax4 = [non_depth_curves[8], non_depth_curves[7], non_depth_curves[1]]
    print(f'ax1: {ax4}')
    ax5 = [non_depth_curves[0]]
    print(f'ax1: {ax5}')

    ax_list = [ax1, ax2, ax3, ax4, ax5]

    return ax_list
