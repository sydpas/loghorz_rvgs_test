import numpy as np
import matplotlib
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

    # tops = ki_ret.sections['TOPS_Data']
    # top_names = []
    # top_values = []
    # for i in tops:
    #     if i.strip():  # if i is not empty (does not have whitespaces)...
    #         i_list = i.split()  # split i into parts based on where there is whitespaces into i_list
    #         if len(i_list) >= 2:  # determines if there is a top name and a top depth
    #             top_names.append(i_list[0])  # stores names
    #             top_values.append(i_list[1])  # stores depths

    print(ki_ret.data)  # shows all curves/logs

    return ki_ret, curve_list, columns









