# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   loading.py                                          :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: vivozzo- <vivozzo-@student.42porto.com>     +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/06/29 14:13:09 by vivozzo-           #+#    #+#             #
#   Updated: 2026/07/03 09:10:47 by vivozzo-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from importlib.metadata import version, PackageNotFoundError


def compare_package_versions() -> bool:

    print("\nChecking dependencies:")

    flag = False

    try:
        print(f"[OK] pandas ({version('pandas')}) - Data manipulation ready")
    except PackageNotFoundError:
        print("pandas: Not installed")
        flag = True

    try:
        print(f"[OK] numpy ({version('numpy')}) - Numerical computation ready")
    except PackageNotFoundError:
        print("numpy: Not installed")
        flag = True

    try:
        print(
            f"[OK] matplotlib ({version('matplotlib')}) - Visualization ready")
    except PackageNotFoundError:
        print("matplotlib: Not installed")
        flag = True

    return flag


def main() -> None:
    print("LOADING STATUS: Loading programs...")

    flag = compare_package_versions()

    if flag is True:
        print("\nExiting the program, install the missing dependencies!")
        print("\nHow to install with pip:")
        print("pip install -r requirements.txt")
        print("python3 loading.py")
        print("\nHow to install with Poetry: ")
        print("poetry install")
        print("poetry run python loading.py")
        return

    from pandas import DataFrame
    from numpy import random
    from matplotlib.pyplot import savefig

    print("\nAnalyzing Matrix data...")
    matrix = random.randint(0, 100, size=(250, 4))

    print("Processing 1000 data points...")
    df = DataFrame(
        matrix,
        columns=["A", "B", "C", "D"]
    )

    print("Generating visualization...")
    df.plot()
    print("\nAnalysis complete!")
    savefig("matrix_analysis.png")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
