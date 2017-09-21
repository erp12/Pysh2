import argparse

from fly import start_n_fly_runs


def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'machine',
        type=str,
        choices=['fly', 'digital_ocean']
    )
    parser.add_argument(
        'file',
        type=str,
        help='Path to problem file realtive to pyshgp root. Likely in examples folder.')
    parser.add_argument(
        'n',
        type=int,
        help='Number of runs to start.',
        default=1)
    return parser.parse_args()


if __name__ == "__main__":
    cli_args = get_cli_args()

    if cli_args.machine == 'fly':
        start_n_fly_runs(cli_args.file, cli_args.n)
    # elif cli_args.machine == 'digital_ocean':
    #     start_n_DO_runs(cli_args.file, cli_args.n)
