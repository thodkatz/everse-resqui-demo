from dataclasses import dataclass

import numpy as np
from scipy.optimize import curve_fit


def logistic(t, capacity, rate, initial):
    """Logistic growth: population at time ``t``."""
    return capacity / (1 + ((capacity - initial) / initial) * np.exp(-rate * t))


@dataclass(frozen=True)
class GrowthFit:
    capacity: float
    rate: float
    initial: float

    @property
    def doubling_time(self):
        """Doubling time during exponential growth, in the units of ``t``."""
        return np.log(2) / self.rate


def fit_logistic(times, values):
    """Fit a logistic curve to ``values`` measured at ``times``."""
    times = np.asarray(times, dtype=float)
    values = np.asarray(values, dtype=float)
    guess = [values.max(), 0.5, max(values.min(), 1e-6)]
    (capacity, rate, initial), _ = curve_fit(logistic, times, values, p0=guess, maxfev=10000)
    return GrowthFit(capacity, rate, initial)
