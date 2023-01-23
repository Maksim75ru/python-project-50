import argparse


def parse_cli():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f FORMAT", "--format FORMAT",
                        help='set format of output', action='store_true')
    args = parser.parse_args()
    return args