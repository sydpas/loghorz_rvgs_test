import pandas as pd
import matplotlib.pyplot as plt
from andy.andy12 import (andy12)
from andy.andy06 import(andy06)


def main():
    """
    This function takes the andy12 and andy06 functions and plots curves with the tops displayed.
    """

    # call bg functions
    columns, non_depth_curves, curve_unit_list, df = andy12()
    well_tops_list = andy06()

    fig, axes = plt.subplots(1, columns, figsize=(columns * 1.2, 12))

    for i, curve in enumerate(non_depth_curves):
        ax = axes[i]
        if i != 0:  # remove depth y labels except for first plot
            ax.set_yticklabels([])
            ax.set_yticks([])
        unit = curve_unit_list[i + 1]
        top = well_tops_list[0]

        # plotting tops
        for horz, depth in top.items():
            if pd.notna(depth):
                y = float(depth)
                ax.axhline(y=y, color='red', lw=2, ls='-')
                # if i == 0:
                #     ax.text(x=20, y=y, s=horz, color='red', fontsize=10, ha='center', va='center')

        if curve != 'GR' and curve != 'PE':
            # plotting curves
            df.plot(
                x=curve, y='DEPTH', color='black', title=curve, ax=ax, xlabel=unit,
                linewidth=0.5, marker='o', markersize='0.2', alpha=0.5, legend=False)
            ax.set_title(curve, fontweight='bold', fontsize=14)
            ax.set_ylim(df['DEPTH'].min(), df['DEPTH'].max())  # ensures the curves have the right limits

        elif curve == 'GR':
            df.plot(
                x='GR', y='DEPTH', color='black', title=curve, ax=ax, xlabel=unit,
                linewidth=0.5, marker='o', markersize='0.2', alpha=0.5, legend=False)
            ax.fill_betweenx(df['DEPTH'], df['GR'], 75, facecolor='yellow')
            ax.fill_betweenx(df['DEPTH'], df['GR'], 0, facecolor='white')
            ax.axvline(75, color='black', linewidth=0.5, alpha=0.5)
            ax.set_title(curve, fontweight='bold', fontsize=14)
            ax.set_ylim(df['DEPTH'].min(), df['DEPTH'].max())

        elif curve == 'PE':
            df.plot(
                x='PE', y='DEPTH', color='black', title=curve, ax=ax, xlabel=unit,
                linewidth=0.5, marker='o', markersize='0.2', alpha=0.5, legend=False)
            ax.set_title(curve, fontweight='bold', fontsize=14)
            ax.set_ylim(df['DEPTH'].min(), df['DEPTH'].max())

    plt.tight_layout()
    plt.savefig('../figures/tops_curves_highres.png')
    plt.show()

if __name__ == "__main__":
    main()
