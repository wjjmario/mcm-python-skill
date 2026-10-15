"""Reproducible synthetic regression demo; replace for actual contest problems."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=root / 'config.json')
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding='utf-8'))
    n, fraction, noise = config['samples'], config['train_fraction'], config['noise_std']
    if not isinstance(n, int) or isinstance(n, bool) or n < 10:
        parser.error('samples must be an integer >= 10')
    if not isinstance(fraction, (float, int)) or not 0.2 <= fraction <= 0.8:
        parser.error('train_fraction must be in [0.2, 0.8]')
    if not isinstance(noise, (float, int)) or not np.isfinite(noise) or noise < 0:
        parser.error('noise_std must be finite and nonnegative')
    rng = np.random.default_rng(config['seed'])
    x = rng.uniform(0, 10, n)
    y = 2 * x + 1 + rng.normal(0, noise, n)
    ids = rng.permutation(n)
    split = int(n * fraction)
    train, test = ids[:split], ids[split:]
    design = np.column_stack((np.ones(n), x))
    beta, _, rank, _ = np.linalg.lstsq(design[train], y[train], rcond=None)
    if rank != 2:
        raise RuntimeError('Regression design is rank deficient')
    predicted = design[test] @ beta
    baseline = np.full(len(test), y[train].mean())
    def rmse(values):
        return float(np.sqrt(np.mean((y[test] - values) ** 2)))
    metrics = {
        'synthetic_demo': True, 'config': config,
        'data_sha256': hashlib.sha256(np.column_stack((x, y)).tobytes()).hexdigest(),
        'intercept': float(beta[0]), 'slope': float(beta[1]),
        'test_rmse': rmse(predicted), 'baseline_test_rmse': rmse(baseline),
        'test_samples': len(test),
        'environment': {'python': sys.version, 'platform': platform.platform(),
                        'numpy': np.__version__, 'matplotlib': matplotlib.__version__}}
    for directory in ('results', 'figures', 'data/processed'):
        (root / directory).mkdir(parents=True, exist_ok=True)
    np.savetxt(root / 'data/processed/synthetic-demo.csv', np.column_stack((x, y)),
               delimiter=',', header='x,y', comments='')
    np.savetxt(root / 'results/test-predictions.csv',
               np.column_stack((test, x[test], y[test], predicted, baseline)),
               delimiter=',', header='row,x,observed,predicted,baseline', comments='')
    (root / 'results/metrics.json').write_text(json.dumps(metrics, indent=2, allow_nan=False)+'\n', encoding='utf-8')
    fig, ax = plt.subplots(figsize=(6, 4), constrained_layout=True)
    ax.scatter(x[test], y[test], label='Held-out synthetic data', color='#0072B2')
    grid = np.linspace(0, 10, 100)
    ax.plot(grid, beta[0]+beta[1]*grid, label='Fitted model', color='#D55E00')
    ax.set(xlabel='x (arbitrary units)', ylabel='y (arbitrary units)', title='Synthetic demo: not contest evidence')
    ax.legend()
    fig.savefig(root / 'figures/synthetic-demo.png', dpi=300)
    fig.savefig(root / 'figures/synthetic-demo.svg')
    plt.close(fig)
    print(json.dumps({k: metrics[k] for k in ('synthetic_demo', 'test_rmse', 'baseline_test_rmse')}))

if __name__ == '__main__':
    main()
