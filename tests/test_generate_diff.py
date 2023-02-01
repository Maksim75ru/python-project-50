import pytest
from gendifff.engine import generate_diff

json_1 = 'tests/fixtures/file1.json'
json_2 = 'tests/fixtures/file2.json'
yml_1 = 'tests/fixtures/file1.yml'
yml_2 = 'tests/fixtures/file2.yml'

stylish_result = 'tests/fixtures/stylish_result'


formats = ['stylish']


@pytest.mark.parametrize('file1_path, file2_path, format_name, expected', [(json_1, json_2, formats[0], stylish_result),
                                                                           (yml_1, yml_2, formats[0], stylish_result),
                                                                           ])


def test_generate_diff(file1_path, file2_path, format_name, expected):
    with open(expected) as f:
        assert generate_diff(file1_path, file2_path, format_name) == f.read()
