import json
import yaml


FORMATS = {
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load,
}


def get_content(file_data, extension):
    if extension not in FORMATS:
        raise ValueError('Unsupported extension')
    return FORMATS[extension](file_data)
