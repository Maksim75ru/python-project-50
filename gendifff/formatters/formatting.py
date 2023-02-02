from gendifff.formatters import stylish_format


FORMATTERS = {
    'stylish': stylish_format,
}


def formatting(tree, format_name):
    if format_name not in FORMATTERS:
        raise ValueError('Unsupported format')

    return FORMATTERS[format_name].get_diff_format(tree)
