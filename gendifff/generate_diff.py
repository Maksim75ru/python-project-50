import json


def get_format(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def generate_diff(file_path1, file_path2) -> str:
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
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
