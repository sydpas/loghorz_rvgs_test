import pandas as pd
import matplotlib.pyplot as plt
from andy.andy12_mainpass import (andy12)
from andy.andy06 import (andy06)
from assembly_highres import (organize_curves)



def main():
    """
    This function takes the andy12, andy06, and organize_curves functions, and plots all groups of combined curves with
    the tops displayed, and adds background grids.
    """

    # calling all bg functions
    global current_ax
    _, _, _, df = andy12()
    well_tops_list = andy06()
    ax_list, col_list = organize_curves()

    print(f'Groups: {ax_list}')
    print(f'Columns: {col_list}')

    fig, axes = plt.subplots(1, len(ax_list), figsize=(len(ax_list) * 5, 14))

    # zip pairs up elements from 2 lists and brings them together
    for i, (curves, ax) in enumerate(zip(ax_list, axes)):
        print(f'Plotting group: {curves}...')
        top = well_tops_list[0]
        for horz, depth in top.items():
            if pd.notna(depth):
                y = float(depth)
                ax.axhline(y=y, color='red', lw=2, ls='-')

        if i == 3 and len(curves) == 3:  # handling the fourth group
            ax2 = ax.twiny()
            ax3 = ax.twiny()


            for j, curve in enumerate(curves):
                print(f'Plotting curve: {curve}...')
                if curve == 'PE':
                    current_ax = ax
                elif curve == 'RHOB':
                    current_ax = ax2
                elif curve == 'GR':
                    current_ax = ax3

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

                else:
                    df.plot(
                        x=curve, y='DEPTH', color='blue', ax=current_ax, label=curve,
                        linewidth=0.5, marker='o', markersize=0.2, alpha=0.5)

            # adjusting proper y limits
            ax.set_ylim(df['DEPTH'].min(), df['DEPTH'].max())
            # x axis limits
            ax.set_xlim(df[curves[0]].min(), df[curves[0]].max())
            ax2.set_xlim(df[curves[1]].min(), df[curves[1]].max())
            ax3.set_xlim(df[curves[2]].min(), df[curves[2]].max())

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
            ax.set_title(f'{curves[0]}, {curves[1]} and {curves[2]}', fontweight='bold', fontsize=12)

            continue

        # creating a new x-axis on the top for next curve but for same graph
        ax2 = ax.twiny()

        colors = ['blue', 'purple', 'red', 'green', 'orange']
        color_index = 0

        for j, curve in enumerate(curves):
            print(f'Plotting curve: {curve}...')
            if curve == 'GR':
                df.plot(
                    x=curve, y='DEPTH', color='black', ax=ax,
                    linewidth=0.5, marker='o', markersize=0.2, alpha=0.5, label='GR')
                ax.fill_betweenx(df['DEPTH'], df[curve], 75, facecolor='yellow')
                ax.fill_betweenx(df['DEPTH'], df[curve], 0, facecolor='white')
                ax.axvline(75, color='black', linewidth=0.5, alpha=0.5)

            else:
                next_ax = ax2 if j > 0 and ax2 else ax
                df.plot(
                    x=curve, y='DEPTH', color=colors[color_index], ax=next_ax, label=curve,
                    linewidth=0.5, marker='o', markersize=0.2, alpha=0.5)

        # adjusting proper y limits and x limits
        ax.set_ylim(df['DEPTH'].min(), df['DEPTH'].max())
        ax.set_xlim(df[curves[0]].min(), df[curves[0]].max())
        if ax2:
            ax2.set_xlim(df[curves[-1]].min(), df[curves[-1]].max())

        # removing x axis which sometimes works...
        ax.set_xlabel('')
        if ax2:
            ax2.set_xlabel('')

        # combining the legends and putting bottom left
        if ax2:
            lines_1, labels_1 = ax.get_legend_handles_labels()
            lines_2, labels_2 = ax2.get_legend_handles_labels()
            ax.legend(lines_1 + lines_2, labels_1 + labels_2, loc='lower left')
            ax2.get_legend().remove() if ax2.get_legend() else None

        ax.grid(True, linestyle='-', alpha=0.3, linewidth=0.5)
        ax.set_title(' & '.join(curves), fontweight='bold', fontsize=12)

    plt.tight_layout()
    plt.savefig(f'../figures/all_log2.png')
    plt.show()


if __name__ == "__main__":
    main()