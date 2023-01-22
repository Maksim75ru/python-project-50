import json


def generate_diff(file_path1, file_path2) -> str:
    file1 = dict(sorted(json.load(open(str(file_path1))).items(), key=lambda x: x[0]))
    file2 = dict(sorted(json.load(open(str(file_path2))).items(), key=lambda x: x[0]))

    result = ''
    for key1 in file1:
        value1 = file1.get(key1, None)
        if isinstance(value1, bool):
            value1 = str(value1).lower()

        if key1 not in file2:
            result += f' - {key1}: {value1}\n'
        else:
            value2 = file2.get(key1, None)
            if value1 == value2:
                result += f'   {key1}: {value1}\n'
                file2.pop(key1)
            else:
                result += f' - {key1}: {value1}\n'
                result += f' + {key1}: {value2}\n'
                file2.pop(key1)

    for key2 in file2:
        value2 = file2.get(key2, None)
        if isinstance(value2, bool):
            value2 = str(value2).lower()

        result += f' + {key2}: {value2}\n'

    return '{\n' + result + '}'
