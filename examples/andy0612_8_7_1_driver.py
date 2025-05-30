import pandas as pd
import matplotlib.pyplot as plt
from andy.andy12_highres import (andy12)
from andy.andy06 import (andy06)
from assembly_highres import (organize_curves)



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

    fig, ax = plt.subplots(figsize=(col1 * 3, 14))

    top = well_tops_list[0]
    for horz, depth in top.items():
        if pd.notna(depth):
            y = float(depth)
            ax.axhline(y=y, color='red', lw=2, ls='-')

    # creating new x axes
    ax2 = ax.twiny()
    ax3 = ax.twiny()
    axes = [ax, ax2, ax3]

    for i, curve in enumerate(ax1):
        print(f'Plotting curve: {curve}...')
        current_ax = axes[i]
        if curve == 'GR':
            df.plot(
                x='GR', y='DEPTH', color='black', ax=current_ax,
                linewidth=0.5, marker='o', markersize=0.2, alpha=0.5, label='GR')

            gr_min = df[curve].min()
            gr_max = df[curve].max()

            current_ax.fill_betweenx(df['DEPTH'], df[curve], 75,
                                     where=(df[curve] <= 75),
                                     facecolor='yellow', alpha=0.5)

            current_ax.fill_betweenx(df['DEPTH'], df[curve], gr_max,
                                     where=(df[curve] > 75),
                                     facecolor='white', alpha=0.5)

            current_ax.axvline(75, color='black', linewidth=0.5, alpha=0.5)
            current_ax.set_xlim(gr_min, gr_max)
            print(f'{i} curve: {curve}')

        else:
            df.plot(
                x=curve, y='DEPTH', color='blue', ax=current_ax, label=curve,
                linewidth=0.5, marker='o', markersize=0.2, alpha=0.5)
            print(f'{i} curve: {curve}')


    # adjusting proper y limits
    ax.set_ylim(df['DEPTH'].min(), df['DEPTH'].max())
    # x axis limits
    ax.set_xlim(df[ax1[0]].min(), df[ax1[0]].max())
    ax2.set_xlim(df[ax1[1]].min(), df[ax1[1]].max())
    ax3.set_xlim(df[ax1[2]].min(), df[ax1[2]].max())

    # removing x axis
    ax.set_xlabel('')
    ax2.set_xlabel('')
    ax3.set_xlabel('')

    # combining the legends and putting bottom left
    lines_1, labels_1 = ax.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    lines_3, labels_3 = ax3.get_legend_handles_labels()
    ax.legend(lines_1 + lines_2 + lines_3, labels_1 + labels_2 + labels_3, loc='lower left')
    ax2.get_legend().remove() if ax2.get_legend() else None
    ax3.get_legend().remove() if ax3.get_legend() else None

    ax.grid(True, linestyle='-', alpha=0.3, linewidth=0.5)
    ax.set_title(f'{ax1[0]}, {ax1[1]} and {ax1[2]}', fontweight='bold', fontsize=14)

    plt.tight_layout()
    plt.savefig(f'../figures/PERHOBGR_log.png')
    plt.show()


if __name__ == "__main__":
    main()