import matplotlib
matplotlib.use('TkAgg')  # TkAgg is a backend that determines how plots are displayed
import matplotlib.pyplot as plt
from welly import Well
import welly.quality as q

# load LAS file
well = Well.from_las('C:/Users/sydne/git/rvgs/loghorz_rvgs_test/las_files/HighResolution_full_SelCrv.LAS')

# display basic info
print(well)
print('Header:')
print(well.header)
print(well.location)

gr = well.data['GR']
print(f'Gamma {gr}')

# plotting...
gr.plot()
plt.savefig(f"../../figures/gamma_plot.png")  # use ../../ for 2 away
plt.show()


# alias names: mapping what we want to call curves to mnemonics
alias = {
    "Gamma": ["GR", "GAM", "GRC", "SGR", "NGT"],
    "Density": ["RHOZ", "RHOB", "DEN", "RHOZ"],
    "Sonic": ["DT", "AC", "DTP", "DT4P"]
}

# now we show each measurement (gamma, density, sonic) at various depths
print(well.df(keys=['Gamma', 'Density', 'Sonic'], alias=alias))

# to identify the middle of the well, we can use a basis
print('Looking at a depth of 800-820m...')
basis = range(800, 821)
print(well.df(keys=['Gamma', 'Density', 'Sonic'], alias=alias, basis=basis))


tests = {
    'Each': [
        q.no_flat,  # ensures no constant (flat) values
        q.no_monotonic,  # no strict increase/decrease
        q.no_gaps,  # no missing values
    ],
    'Gamma': [
        q.all_positive,  # all positive values
        q.all_below(450),  # all values are below 450
        q.check_units(['API', 'GAPI']),  # checks curve units
    ],
    'DT': [
        q.all_positive,  # ensures all values are positive (time or velocity)
    ],
    'Sonic': [
        q.all_between(1, 10000),  # ensures velocity is between 1-10000
        q.no_spikes(10),  # allows 10 outliers
    ],
}

print('Now testing the quality of curves using predefined tests...')
passed = well.qc_data(tests, alias=alias)
print(passed)



