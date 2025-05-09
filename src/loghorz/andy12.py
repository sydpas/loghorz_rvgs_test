import matplotlib.pyplot as plt
import lasio


def andy12():
    """
    This function reads an LAS file and prints various information.

    Returns:
         columns: length of non_depth_curves list.
         non_depth_curves: list of curves without depth.
         curve_unit_list: list of all curve units excluding depth.
         df: the LAS file converted to a pandas DataFrame.
    """
    las = lasio.read("../../las_files/HighResolution_full_SelCrv.LAS")

    df = las.df()  # convert to pandas dataframe
    df['DEPTH'] = df.index  # adding depth column
    # print(f'df describe: {df.describe()}')  # prints stats

    curve_list = las.curves
    # print(f'curve list: {curve_list}')

    # mapping curve mnemonic to descrip
    curve_name_dict = {curve.mnemonic: curve.descr for curve in las.curves}
    # print(f'dictionary: {curve_name_dict}')

    # making list of units
    curve_unit_list = []
    for curve in curve_list:
        curve_unit_list.append(curve.unit)
    # print(f'units: {curve_unit_list}')

    non_depth_curves = [
        curve_name.mnemonic for curve_name in curve_list if curve_name.mnemonic != 'DEPT'
            and curve_name.mnemonic in df.columns]
    # removing the DEPT curve

    columns = len(non_depth_curves)

    return columns, non_depth_curves, curve_unit_list, df


def main():
    """
    This function takes the andy12 and andy06 functions and plots curves.
    """

    columns, non_depth_curves, curve_unit_list, df = andy12()

    fig, axes = plt.subplots(1, columns, figsize=(columns * 1.2, 12))

    for i, curve in enumerate(non_depth_curves):
        ax = axes[i]
        if i != 0:  # remove depth y labels except for first plot
            ax.set_yticklabels([])
            ax.set_yticks([])
        unit = curve_unit_list[i + 1]

        if curve != 'GR' and curve != 'PE':
            df.plot(
                x=curve, y='DEPTH', color='black', title=curve, ax=ax, xlabel=unit,
                linewidth=0.5, marker='o', markersize='0.2', alpha=0.5, legend=False)
            ax.set_title(curve, fontweight='bold', fontsize=14)
        elif curve == 'GR':
            df.plot(
                x='GR', y='DEPTH', color='black', title=curve, ax=ax, xlabel=unit,
                linewidth=0.5, marker='o', markersize='0.2', alpha=0.5, legend=False)
            ax.fill_betweenx(df['DEPTH'], df['GR'], 75, facecolor='yellow')
            ax.fill_betweenx(df['DEPTH'], df['GR'], 0, facecolor='white')
            ax.axvline(75, color='black', linewidth=0.5, alpha=0.5)
            ax.set_title(curve, fontweight='bold', fontsize=14)
        elif curve == 'PE':
            df.plot(
                x='PE', y='DEPTH', color='black', title=curve, ax=ax, xlabel=unit,
                linewidth=0.5, marker='o', markersize='0.2', alpha=0.5, legend=False)
            ax.set_title(curve, fontweight='bold', fontsize=14)

    plt.tight_layout()
    plt.savefig('../../figures/filled_highres.png')
    plt.show()

if __name__ == '__main__':
    main()
