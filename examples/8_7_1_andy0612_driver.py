import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
from andy.andy12 import (andy12)
from andy.andy06 import (andy06)
from assembly import (organize_curves)


def main():
    """
    This function takes the andy12, andy06, and organize_curves functions, and plots PE, RHOB, and GR curves with the
    tops displayed, and adds background grids.
    """

    # calling all bg functions
    _, _, _, df = andy12()
    well_tops_list = andy06()
    ax_list, col_list = organize_curves()

    print(f'Groups: {ax_list}')
    print(f'Columns: {col_list}')

    # plotting the fourth group
    ax1 = ax_list[3]
    col1 = col_list[3]

    fig, ax = plt.subplots(figsize=(col1 * 1.2, 14))

    top = well_tops_list[0]
    for horz, depth in top.items():
        if pd.notna(depth):
            y = float(depth)
            ax.axhline(y=y, color='red', lw=2, ls='-')

    # creating new x axes
    ax2 = ax.twiny()
    ax3 = ax.twiny()

    for curve in ax1:
        print(f'Plotting curve: {curve}...')
        if curve == 'GR':
            df.plot(
                x='GR', y='DEPTH', color='black', ax=ax,
                linewidth=0.5, marker='o', markersize=0.2, alpha=0.5, label='GR')
            ax.fill_betweenx(df['DEPTH'], df['GR'], 75, facecolor='yellow')
            ax.fill_betweenx(df['DEPTH'], df['GR'], 0, facecolor='white')
            ax.axvline(75, color='black', linewidth=0.5, alpha=0.5)
        else:
            df.plot(
                x=curve, y='DEPTH', color='blue', ax=ax2, label=curve,
                linewidth=0.5, marker='o', markersize=0.2, alpha=0.5)



if __name__ == "__main__":
    main()