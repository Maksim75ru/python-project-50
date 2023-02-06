from gendiff.parser import get_content
from gendiff.diff_tree import get_diff
from gendiff.formatters.formatting import formatting
import os


def get_format(file_path: str) -> str:
    extension = os.path.splitext(file_path)[1].lstrip('.')
    return extension


def generate_diff(file_path1: str, file_path2: str, format_name='stylish'):
    file1 = get_content(open(file_path1), get_format(file_path1))
    file2 = get_content(open(file_path2), get_format(file_path2))
    differences = get_diff(file1, file2)

    return formatting(differences, format_name)
