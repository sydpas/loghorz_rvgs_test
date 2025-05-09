import pandas as pd
import matplotlib.pyplot as plt
from andy.andy12 import (andy12)
from andy.andy06 import (andy06)
from assembly import (organize_curves)


def main():
    """
    This function takes the andy12, andy06, and organize_curves functions and plots combined curves with the tops
    displayed, and adds background grids.
    """

    # call bg functions
    _, _, _, df = andy12()
    well_tops_list = andy06()
    ax_list, col_list = organize_curves()

    print(f'Groups: {ax_list}')
    print(f'Columns: {col_list}')

    # just plotting first group for trouble shooting
    ax1 = ax_list[0]
    col1 = col_list[0]

    fig, ax = plt.subplots( figsize=(col1 * 1.2, 12))

    top = well_tops_list[0]
    for horz, depth in top.items():
        if pd.notna(depth):
            y = float(depth)
            ax.axhline(y=y, color='red', lw=2, ls='-')

    # creating a new axis but for same graph
    ax2 = ax.twiny()

    for curve in ax1:
        print(f'Plotting curve: {curve}...')
        if curve == 'GR':
            df.plot(
                x='GR', y='DEPTH', color='black', ax=ax,
                linewidth=0.5, marker='o', markersize=0.2, alpha=0.5, legend=False)
            ax.fill_betweenx(df['DEPTH'], df['GR'], 75, facecolor='yellow')
            ax.fill_betweenx(df['DEPTH'], df['GR'], 0, facecolor='white')
            ax.axvline(75, color='black', linewidth=0.5, alpha=0.5)
            ax.set_xlabel('GR')
        else:
            df.plot(
                x=curve, y='DEPTH', color='blue', ax=ax2,
                linewidth=0.5, marker='o', markersize=0.2, alpha=0.5, legend=False)
            ax2.set_xlabel(curve)

    ax.set_ylim(df['DEPTH'].min(), df['DEPTH'].max())

    # x axis limits
    ax.set_xlim(df[ax1[0]].min(), df[ax1[0]].max())
    ax2.set_xlim(df[ax1[1]].min(), df[ax1[1]].max())

    ax.grid(True, linestyle='-', alpha=0.3, linewidth=0.5)
    ax.set_title(f'{ax1[0]} and {ax1[1]}', fontweight='bold', fontsize=14)

    plt.tight_layout()
    plt.savefig(f'../figures/GRSP_log.png')
    plt.show()


if __name__ == "__main__":
    main()