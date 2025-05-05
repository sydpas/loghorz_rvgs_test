from src.loghorz.logloader_allwell import (
    highres_well,
    mainpass_well,
    repsec_well
)


import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # TkAgg is a backend that determines how plots are displayed


def main():
    # call functions
    all_wells = [(highres_well()), (mainpass_well()), (repsec_well())]  # create a list of 3 tuples

    for well_i, (well, curve_list, columns) in enumerate(all_wells):
        # now we plot...
        fig, axes = plt.subplots(1, columns, figsize=(columns * 1.2, 7))

        for i, curve in enumerate(curve_list):
            ax = axes[i]
            # plot ith curve
            well.data[curve].plot(
                ax, linestyle='-', linewidth=1, color=f'C{i}', marker='o', markersize=0.5, alpha=0.4)
            ax.set_title(f'{curve} Log', fontsize=12, fontweight='bold')
            ax.grid(True, linestyle='-', alpha=0.3, linewidth=0.5)
            ax.tick_params(axis='x', rotation=0)

        plt.tight_layout()
        plt.savefig(f"../figures/{well_i}_plot.png")  # use ../ not .../
        plt.show()


if __name__ == "__main__":
    main()
