import json
import yaml
from yaml.loader import SafeLoader


def get_format(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def get_content(file_path1, file_path2):
    file1 = file2 = ''
    if file_path1.endswith('.json') or file_path2.endswith('.json'):
        file1 = json.load(open(file_path1))
        file2 = json.load(open(file_path2))
    if file_path1.endswith('.yaml') or file_path2.endswith('.yaml') \
            or file_path1.endswith('.yml') or file_path2.endswith('.yml'):
        file1 = yaml.load(open(file_path1), Loader=SafeLoader)
        file2 = yaml.load(open(file_path2), Loader=SafeLoader)

    return file1, file2


def generate_diff(file_path1: str, file_path2: str) -> str:
    file1, file2 = get_content(file_path1, file_path2)

    file1_sorted = dict(sorted(file1.items(), key=lambda x: x[0]))
    file2_sorted = dict(sorted(file2.items(), key=lambda x: x[0]))

    result = ''
    for key1 in file1_sorted:
        value1 = get_format(file1_sorted.get(key1, None))
        value2 = get_format(file2_sorted.get(key1, None))

        if key1 not in file2_sorted:
            result += f' - {key1}: {value1}\n'
        else:
            if value1 == value2:
                result += f'   {key1}: {value1}\n'
            else:
                result += f' - {key1}: {value1}\n'
                result += f' + {key1}: {value2}\n'
            file2_sorted.pop(key1)

    for key2 in file2_sorted:
        value2 = get_format(file2_sorted.get(key2, None))
        result += f' + {key2}: {value2}\n'

    return '{\n' + result + '}'
