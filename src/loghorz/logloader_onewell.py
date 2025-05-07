import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # TkAgg is a backend that determines how plots are displayed
import matplotlib.pyplot as plt
import welly
from welly import Well

def ki_ret_well():
    # load LAS file
    ki_ret = Well.from_las(
                     r"C:\Users\sydne\git\rvgs\loghorz_rvgs_test\las_files\HighResolution_full_SelCrv.LAS")

    # display basic info
    print(ki_ret)
    print('Header:')
    print(ki_ret.header)
    print(ki_ret.location)

    # curves to be plotted
    curve_list = ki_ret.data
    columns = len(curve_list)

    print(ki_ret.data)  # shows all curves/logs

    return ki_ret, curve_list, columns









