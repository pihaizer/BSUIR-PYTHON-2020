import re

FLAGS = re.DOTALL | re.MULTILINE | re.VERBOSE

STRINGCHUNK = re.compile(r'(.*?)(["\\\x00-\x1f])', FLAGS)
NUMBER = re.compile(r'(-?(?:0|[1-9]\d*))(\.\d+)?([eE][-+]?\d+)?', FLAGS)

BACKSLASH_DICT = {
    '"': '"', '\\': '\\', '/': '/',
    'b': '\b', 'f': '\f', 'n': '\n', 'r': '\r', 't': '\t',
}


class JSONDecoderError(ValueError):
    def __init__(self, msg, json_str, pos):
        lineno = json_str.count('\n', 0, pos) + 1
        colno = pos - json_str.rfind('\n', 0, pos)
        error_msg = '{0}: line {1} column {2} (char {3})'.format(msg, lineno, colno, pos)
        super().__init__(error_msg)


def decode_string(s, backslash=BACKSLASH_DICT, chunk_match=STRINGCHUNK.match):
    """Scan the string s for a JSON string."""

    chunks = []
    begin, end = 0, 1
    while True:
        chunk = chunk_match(s, end)
        if chunk is None:
            raise JSONDecoderError('Unterminated string starting at', s, begin)
        end = chunk.end()
        content, terminator = chunk.groups()
        if content:
            chunks.append(content)
        if terminator == '"':
            break
        elif terminator != '\\':
            raise JSONDecoderError('Invalid control character {!r} at'.format(terminator), s, end - 1)
        try:
            esc = s[end]
        except IndexError:
            raise JSONDecoderError('Unterminated string starting at', s, begin) from None
        try:
            char = backslash[esc]
        except KeyError:
            raise JSONDecoderError('Invalid \\escape: {!r}'.format(esc), s, end - 1)
        end += 1
        chunks.append(char)

    return ''.join(chunks)


def decode_array(json_array):
    sep = ', '
    arr = json_array[1:-1].split(sep)
    for idx in range(len(arr)):
        if idx == len(arr):
            break
        c1 = arr[idx].count('[')
        c2 = arr[idx].count(']')
        c3 = arr[idx].count('{')
        c4 = arr[idx].count('}')
        if c1 > c2 >= 0 or c3 > c4 >= 0:
            while c1 != c2 or c3 != c4:
                try:
                    arr[idx] += sep + arr[idx + 1]
                    del arr[idx + 1]
                except IndexError:
                    raise JSONDecoderError('Unterminated json array starting at', json_array, 0) from None
                c1 = arr[idx].count('[')
                c2 = arr[idx].count(']')
                c3 = arr[idx].count('{')
                c4 = arr[idx].count('}')

    python_list = []
    for s in arr:
        if s != '':
            obj = from_json(s)
            python_list.append(obj)

    return python_list


def decode_object(json_obj):
    python_dict = {}
    item_sep = ', '
    key_sep = ': '
    arr = json_obj[1:-1].split(item_sep)
    idx = 0
    while idx != len(arr) - 1:
        next_idx = idx + 1
        c1 = arr[idx].count('{')
        c2 = arr[idx].count('}')
        if arr[next_idx].count(key_sep) and c1 == c2:
            idx += 1
        else:
            arr[idx] += item_sep + arr[next_idx]
            del arr[next_idx]

    for item in arr:
        res = item.split(key_sep)
        if len(res) >= 2:
            key, val = from_json(res[0]), res[1]
            if not isinstance(key, str):
                raise JSONDecoderError('Expecting property name enclosed in double quotes',
                                       json_obj, json_obj.index(res[0]))
            for i in range(2, len(res)):
                val += key_sep + res[i]
            python_dict[key] = from_json(val)
        else:
            raise JSONDecoderError('Invalid json object starting at', json_obj, 0)

    return python_dict


def decode_number(num, number_match):
    idx = 0
    match = number_match(num, idx)
    if match is not None:
        integer, frac, exp = match.groups()
        valid_str = ''
        for item in match.groups():
            if item:
                valid_str += str(item)
        if num != valid_str:
            return None
        if frac or exp:
            res = float(integer + (frac or '') + (exp or ''))
        else:
            res = int(integer)
        return res
    elif num == 'NaN':
        return float('nan')
    elif num == 'Infinity':
        return float('inf')
    elif num == '-Infinity':
        return float('-inf')
    else:
        return None


def from_json(json_string):
    """Deserialize a JSON formatted string to a Python object."""

    if json_string.startswith('"') and json_string.endswith('"'):
        return decode_string(json_string)
    elif json_string == 'null':
        return None
    elif json_string == 'true':
        return True
    elif json_string == 'false':
        return False
    elif json_string.startswith('[') and json_string.endswith(']'):
        return decode_array(json_string)
    elif json_string.startswith('{') and json_string.endswith('}'):
        return decode_object(json_string)
    else:
        number = decode_number(json_string, NUMBER.match)
        if number is not None:
            return number
        raise JSONDecoderError('Invalid JSON string', json_string, 0)
