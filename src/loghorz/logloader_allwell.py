from welly import Well


def highres_well():
    # load LAS file
    highres = Well.from_las(
        r"C:\Users\sydne\git\rvgs\loghorz_rvgs_test\las_files\HighResolution_full_SelCrv.LAS")

    # display basic info
    print(highres)
    print('Header:')
    print(highres.header)
    print(highres.location)

    # curves to be plotted
    curve_list = ['DT', 'GR', 'GRX', 'ILD', 'ILM', 'SFL', 'SP', 'RHOB', 'PE']
    columns = len(curve_list)

    return highres, curve_list, columns

def mainpass_well():
    # load LAS file
    mainpass = Well.from_las(
        r"C:\Users\sydne\git\rvgs\loghorz_rvgs_test\las_files\MainPass_full_SelCrv.LAS")

    # display basic info
    print(mainpass)
    print('Header:')
    print(mainpass.header)
    print(mainpass.location)

    # curves to be plotted
    curve_list = ['GRX', 'DT', 'GR', 'ILD', 'ILM', 'SFL', 'SP', 'RHOB', 'PE']
    columns = len(curve_list)

    return mainpass, curve_list, columns

def repsec_well():
    # load LAS file
    repsec = Well.from_las(
        r"C:\Users\sydne\git\rvgs\loghorz_rvgs_test\las_files\RepeatSection_full_SelCrv.LAS")

    # display basic info
    print(repsec)
    print('Header:')
    print(repsec.header)
    print(repsec.location)

    # curves to be plotted
    curve_list = ['DT', 'GR', 'ILD', 'ILM', 'SFL', 'SP', 'RHOB', 'PE']
    columns = len(curve_list)

    return repsec, curve_list, columns




