from math import isinf, isnan
import re

ESCAPE = re.compile(r'[\x00-\x1f\\"\b\f\n\r\t]')
ESCAPE_DICT = {
    '\\': '\\\\', '"': '\\"',
    '\b': '\\b', '\f': '\\f', '\n': '\\n', '\r': '\\r', '\t': '\\t',
}

for i in range(0x20):
    ESCAPE_DICT.setdefault(chr(i), '\\u{0:04x}'.format(i))


def to_json(obj):
    """Serialize Python object to a JSON formatted string."""

    if isinstance(obj, bool):
        if obj:
            return 'true'
        else:
            return 'false'
    elif isinstance(obj, str):
        return encode_string(obj, ESCAPE, ESCAPE_DICT)
    elif obj is None:
        return 'null'

    # The RFC does not permit the representation of infinite or NaN number values.
    # Despite that, this module accepts and outputs Infinity, -Infinity, and NaN
    # as if they were valid JSON number literal values
    elif isinstance(obj, (int, float)):
        if isinf(obj):
            if obj > 0:
                return 'Infinity'
            else:
                return '-Infinity'
        elif isnan(obj):
            return 'NaN'
        return str(obj)
    elif isinstance(obj, (list, tuple)):
        array = ''
        sep = ', '
        is_separate = False
        for item in obj:
            if is_separate:
                array += sep
            array += to_json(item)
            is_separate = True
        return f'[{array}]'
    elif isinstance(obj, dict):
        json_obj = ''
        key_sep = ': '
        item_sep = ', '
        is_separate = False
        for key, val in obj.items():
            if is_separate:
                json_obj += item_sep
            if isinstance(key, (str, int, float, bool)) or key is None:
                json_key = to_json(key) if isinstance(key, str) else f'"{to_json(key)}"'
            else:
                raise TypeError(f'keys must be str, int, float, bool or None, not {type(key).__name__}')
            json_obj += json_key + key_sep + to_json(val)
            is_separate = True
        return '{%s}' % json_obj
    else:
        raise TypeError(f'Object of type {type(obj).__name__} is not JSON serializable.')


def encode_string(obj, esc=ESCAPE, esc_dict=ESCAPE_DICT):
    def replace(match):
        return esc_dict[match.group(0)]

    return '"{}"'.format(esc.sub(replace, obj))
