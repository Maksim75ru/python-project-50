def get_diff(tree1: dict, tree2: dict) -> dict:  # noqa: C901
    result = {}

    old_keys = set(tree1.keys()) - set(tree2.keys())
    for key in old_keys:
        result[key] = {'status': 'removed', 'value': tree1[key]}

    new_keys = set(tree2.keys()) - set(tree1.keys())
    for key in new_keys:
        result[key] = {'status': 'added', 'value': tree2[key]}

    for key in tree1.keys() and tree2.keys():
        old_val = tree1.get(key, 'not_exists')
        new_val = tree2.get(key, 'not_exists')

        if isinstance(old_val, dict) and isinstance(new_val, dict):
            result[key] = \
                {'status': 'nested', 'value': get_diff(old_val, new_val)}
        elif old_val == new_val:
            result[key] = {'status': 'unchanged', 'value': old_val}
        elif old_val != new_val and old_val == 'not_exists':
            result[key] = {'status': 'added', 'value': new_val}
        else:
            result[key] = {'status': 'changed',
                           'old_value': old_val, 'new_value': new_val}

    return dict(sorted(result.items()))
