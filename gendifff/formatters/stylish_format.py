from gendifff.formatters.normalize_data import normalize_values


def get_string_value(node, depth: int) -> str:
    structure = ['{']
    indent = '  '
    if not isinstance(node, dict):
        return node
    for k, v in node.items():
        structure.append(f"\n{indent * depth}  {k}: {get_string_value(v, depth + 2)}")
    structure.append(f'\n{indent * (depth - 1)}}}')
    return ''.join(structure)


def get_stylish(diff: dict, depth: int = 1) -> str:
    lines = []
    status_key = {
        'unchanged': '  ',
        'removed': '- ',
        'added': '+ ',
    }
    indent = '  '

    for key, val in diff.items():
        status = val['status']

        if status == 'nested':
            lines.append(f"{indent * depth}  {key}: {{\n")
            lines.append(f"{get_stylish(val['value'], depth + 2)}")
            lines.append(f"{indent * (depth + 1)}}}\n")
        elif status == 'changed':
            lines.append(f"{indent * depth}- {key}: "
                         f"{get_string_value(val['old_value'], depth + 2)}\n")
            lines.append(f"{indent * depth}+ {key}: "
                         f"{get_string_value(val['new_value'], depth + 2)}\n")
        else:
            lines.append(f"{indent * depth}{status_key[status]}{key}: "
                         f"{get_string_value(val['value'], depth + 2)}\n")

    return ''.join(lines)


def get_diff_format(diff: dict) -> str:
    diff = normalize_values(diff)
    return f"{{\n{get_stylish(diff, 1)}}}"
