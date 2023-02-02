def normalize_values(data: dict) -> dict:
    correct_values = {
        None: 'null',
        False: 'false',
        True: 'true',
        '': 'null',
        ' ': 'null'
    }

    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, dict):
                normalize_values(v)
            elif isinstance(v, (bool, type(None))) or \
                    v in correct_values.keys():
                data[k] = correct_values[v]
    return data
