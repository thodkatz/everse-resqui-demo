import numpy as np
import pytest

from growthcurve import fit_logistic, logistic


def test_logistic_starts_at_initial_value():
    assert logistic(0.0, 2.0, 0.5, 0.1) == pytest.approx(0.1)


def test_logistic_approaches_capacity():
    assert logistic(100.0, 2.0, 0.5, 0.1) == pytest.approx(2.0)


def test_fit_recovers_known_parameters():
    times = np.linspace(0, 12, 25)
    values = logistic(times, 1.3, 0.7, 0.05)
    fit = fit_logistic(times, values)
    assert fit.capacity == pytest.approx(1.3, rel=1e-3)
    assert fit.rate == pytest.approx(0.7, rel=1e-3)
    assert fit.doubling_time == pytest.approx(np.log(2) / 0.7, rel=1e-3)
