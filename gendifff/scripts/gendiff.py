from gendifff import generate_diff
from gendifff.cli import parse_cli


def main():
    print(parse_cli())
    # diff = generate_diff(path_file1, path_file2)
    # print(diff)


if __name__ == '__main__':
    main()
