import argparse
from console import run
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Progressive console game; complete TODO 1→2→3 in game.py.')
    parser.add_argument('--seed', type=int, default=None, help='Optional reproducible initial state')
    args = parser.parse_args()
    run(seed=args.seed)
