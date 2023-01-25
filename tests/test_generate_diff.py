import os
from gendifff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


plain_data = read(get_fixture_path('plain.txt')).rstrip()


def test_generate_diff():
    expected = plain_data
    assert generate_diff('source/file1.json', 'source/file2.json') == expected
    assert generate_diff('source/file1.yml', 'source/file2.yml') == expected
