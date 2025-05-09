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

    for j in range(len(col_list)):
        column = col_list[j]

        print(f'Processing column {column}...')

        fig, axes = plt.subplots(1, column, figsize=(column * 1.2, 12))
        if column == 1:
            axes = [axes]

        print(f'j: {j}')
        ax = axes[0]

        print(f'Processing group {column}...')

        if j != 0:  # remove depth y labels except for first plot
            ax.set_yticklabels([])
            ax.set_yticks([])

        top = well_tops_list[0]

        # plotting tops
        for horz, depth in top.items():
            if pd.notna(depth):
                y = float(depth)
                ax.axhline(y=y, color='red', lw=2, ls='-')
                # if i == 0:
                #     ax.text(x=20, y=y, s=horz, color='red', fontsize=10, ha='center', va='center')

        for curve in column:
            print(f'Plotting curve: {curve}...')
            if curve == 'GR':
                df.plot(
                    x='GR', y='DEPTH', color='black', ax=ax,
                    linewidth=0.5, marker='o', markersize='0.2', alpha=0.5, legend=False)
                ax.fill_betweenx(df['DEPTH'], df['GR'], 75, facecolor='yellow')
                ax.fill_betweenx(df['DEPTH'], df['GR'], 0, facecolor='white')
                ax.axvline(75, color='black', linewidth=0.5, alpha=0.5)
                ax.set_ylim(df['DEPTH'].min(), df['DEPTH'].max())
            elif curve == 'PE':
                df.plot(
                    x='PE', y='DEPTH', color='black', ax=ax,
                    linewidth=0.5, marker='o', markersize='0.2', alpha=0.5, legend=False)
                ax.set_ylim(df['DEPTH'].min(), df['DEPTH'].max())
            elif curve != 'GR' and curve != 'PE':
                if curve in df.columns:
                    df.plot(
                        x=curve, y='DEPTH', color='black', ax=ax,
                        linewidth=0.5, marker='o', markersize='0.2', alpha=0.5, legend=False)
                    ax.set_ylim(df['DEPTH'].min(), df['DEPTH'].max())  # ensures the curves have the right limits

            ax.set_title(curve, fontweight='bold', fontsize=14)
            ax.grid(True, linestyle='-', alpha=0.3, linewidth=0.5)
            ax.set_xlim(df['DEPTH'].min(), df['DEPTH'].max())

        plt.tight_layout()
        # plt.savefig(f'../figures/tops_curves_{group}.png')
        # plt.show()


if __name__ == "__main__":
    main()
