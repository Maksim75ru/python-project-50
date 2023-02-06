from gendiff.formatters.normalize_data import normalize_values


def get_complex_value(val):
    if isinstance(val, dict):
        return '[complex value]'
    elif val in ('null', 'true', 'false') or isinstance(val, (int, float)):
        return val
    return f"'{val}'"


def get_stylish(diff: dict, keys=None) -> str:  # noqa: C901
    lines = []
    parents = ''
    output_msg = {
        'changed': "Property '{path}' was updated. From {old} to {new}",
        'removed': "Property '{path}' was removed",
        'added': "Property '{path}' was added with value: {val}"
    }

    if keys is not None:
        parents += keys + '.'

    for key, val in diff.items():
        status = val['status']

        if status == 'nested':
            lines.append(f"{get_stylish(val.get('value'), parents + key)}")
        else:
            if status == 'changed':
                old_val = get_complex_value(val.get('old_value'))
                new_val = get_complex_value(val.get('new_value'))
                lines.append(output_msg[status].format(
                    path=parents + key,
                    old=old_val,
                    new=new_val))
            if status == 'removed':
                lines.append(output_msg[status].format(path=parents + key))
            if status == 'added':
                work_value = get_complex_value(val.get('value'))
                lines.append(output_msg[status].format(
                    path=parents + key,
                    val=work_value))

    return '\n'.join(lines)


def get_diff_format(diff: dict) -> str:
    diff = normalize_values(diff)
    return get_stylish(diff)
