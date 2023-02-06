from gendiff.formatters import stylish_format, plain_format, json_format


FORMATTERS = {
    'stylish': stylish_format,
    'plain': plain_format,
    'json': json_format,
}


def formatting(tree, format_name):
    if format_name not in FORMATTERS:
        raise ValueError('Unsupported format')

    return FORMATTERS[format_name].get_diff_format(tree)
