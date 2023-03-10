from gendiff.formatters.normalize_data import normalize_values


def get_complex_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value in ('null', 'true', 'false') or isinstance(value, (int, float)):
        return value
    return f"'{value}'"


def get_plain(diff: dict, keys=None) -> str:  # noqa: C901
    lines = []
    parents = ''
    output_msg = {
        'changed': "Property '{path}' was updated. From {old} to {new}",
        'removed': "Property '{path}' was removed",
        'added': "Property '{path}' was added with value: {val}"
    }

    if keys is not None:
        parents += keys + '.'

    for key, value in diff.items():
        status = value['status']

        if status == 'nested':
            lines.append(f"{get_plain(value.get('value'), parents + key)}")
        if status == 'changed':
            old_val = get_complex_value(value.get('old_value'))
            new_val = get_complex_value(value.get('new_value'))
            lines.append(output_msg[status].format(
                path=parents + key,
                old=old_val,
                new=new_val))
        if status == 'removed':
            lines.append(output_msg[status].format(path=parents + key))
        if status == 'added':
            work_value = get_complex_value(value.get('value'))
            lines.append(output_msg[status].format(
                path=parents + key,
                val=work_value))

    return '\n'.join(lines)


def get_diff_format(diff: dict) -> str:
    diff = normalize_values(diff)
    return get_plain(diff)
