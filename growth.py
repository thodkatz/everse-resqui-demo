# fit a logistic growth curve to OD600 measurements
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

df = pd.read_csv("/home/maria/experiments/2024-03/od600.csv")

def f(t, K, r, N0):
    return K / (1 + ((K - N0) / N0) * np.exp(-r * t))

p, _ = curve_fit(f, df.time_h, df.od600, p0=[1.0, 0.5, 0.05])
print("K =", p[0])
print("r =", p[1])
print("doubling time =", np.log(2) / p[1])
