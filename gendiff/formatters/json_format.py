import json


def get_diff_format(diff: dict):
    return json.dumps(diff, indent=4)
