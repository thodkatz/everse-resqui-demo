"""Usage: python -m growthcurve <measurements.csv>

The CSV needs the columns ``time_h`` and ``od600``.
"""

import sys

import pandas as pd

from growthcurve import fit_logistic


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print(__doc__)
        return 2
    data = pd.read_csv(argv[0])
    fit = fit_logistic(data["time_h"], data["od600"])
    print(f"carrying capacity: {fit.capacity:.3f}")
    print(f"growth rate:       {fit.rate:.3f} per hour")
    print(f"doubling time:     {fit.doubling_time:.2f} hours")
    return 0


if __name__ == "__main__":
    sys.exit(main())
