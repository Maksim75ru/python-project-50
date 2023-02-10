def normalize_values(data: dict) -> dict:
    correct_values = {
        None: 'null',
        False: 'false',
        True: 'true',
    }

    for key, value in data.items():
        if isinstance(value, dict):
            normalize_values(value)
        elif isinstance(value, (bool, type(None))):
            data[key] = correct_values[value]
    return data
