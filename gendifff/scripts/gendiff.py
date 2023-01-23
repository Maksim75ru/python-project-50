from gendifff import generate_diff
from gendifff.cli import parse_cli


def main():
    args = parse_cli()
    # diff = generate_diff(args.first_file, args.second_file)
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
