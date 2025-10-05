# src/config_lookup.py

def find_key(obj, target):
    """
    Recursively search through dicts, lists, and tuples to find the first occurrence
    of the given key. Returns the corresponding value, or None if not found.
    """

    if isinstance(obj, dict):
        # Check current dict first
        if target in obj:
            return obj[target]
        # Otherwise recurse into values
        for v in obj.values():
            res = find_key(v, target)
            if res is not None or (target in v if isinstance(v, dict) else False):
                return res

    elif isinstance(obj, (list, tuple)):
        for elem in obj:
            res = find_key(elem, target)
            if res is not None or (target in elem if isinstance(elem, dict) else False):
                return res

    return None
