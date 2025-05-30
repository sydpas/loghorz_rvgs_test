from src.loghorz.logloader_onewell import (
    ki_ret_well
)


import matplotlib.pyplot as plt


def main():
    # call function
    ki_ret, curve_list, columns = ki_ret_well()

    # now we plot...
    fig, axes = plt.subplots(1, columns, figsize=(columns * 1.5, 10))

    for i, curve in enumerate(curve_list):
        ax = axes[i]
        # plot ith curve
        ki_ret.data[curve].plot(
            ax, linestyle='-', linewidth=1, color='black', marker='o', markersize=0.4, alpha=0.5)
        ax.set_title(f'{curve} Log', fontsize=12, fontweight='bold')
        ax.grid(True, linestyle='-', alpha=0.3, linewidth=0.5)
        ax.tick_params(axis='x', rotation=0)

    plt.tight_layout()
    plt.savefig("../figures/ki_ret_plot.png")  # use ../ not .../
    plt.show()


if __name__ == "__main__":
    main()
