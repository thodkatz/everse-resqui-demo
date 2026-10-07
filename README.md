# growthcurve

Fit logistic growth curves to optical density (OD600) measurements and report
the carrying capacity, growth rate and doubling time.

This repository is an example for the
[EOSC Arena software quality action](https://github.com/BiodataAnalysisGroup/eosc-arena-software-quality-action).
Its history shows a small research script being brought up to common quality
indicators, checked on every push.

## Installation

```bash
pip install .
```

Requires Python 3.10 or newer; dependencies are listed in `pyproject.toml`
(and `requirements.txt`).

## Usage

```bash
python -m growthcurve data/od600.csv
```

```python
from growthcurve import fit_logistic

fit = fit_logistic(times, od600)
print(fit.doubling_time)
```

## Citation

Please cite the repository URL.

## License

MIT, see [LICENSE](LICENSE).
