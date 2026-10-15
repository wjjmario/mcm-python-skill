"""Create a new MCM project without overwriting existing directories."""
import argparse
from pathlib import Path
import shutil

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()
    target = args.destination.expanduser().resolve()
    if target.exists():
        parser.error(f'Destination already exists: {target}')
    template = Path(__file__).resolve().parents[1] / 'assets' / 'project'
    shutil.copytree(template, target)
    for directory in ('data/raw', 'data/processed', 'results', 'figures'):
        (target / directory).mkdir(parents=True, exist_ok=True)
    print(f'Created: {target}. Included program is a synthetic demo, not a contest answer.')

if __name__ == '__main__':
    main()
