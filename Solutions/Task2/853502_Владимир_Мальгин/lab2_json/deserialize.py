import re

from .exceptions import InvalidJsonException
from .utility import skip_recursively, skip_str


def deserialize(arg: str):
    s = arg.replace('\n', '')
    s = s.strip()
    if s.startswith('[') and s.endswith(']'):
        return deserialize_list(s)
    elif s.startswith('{') and s.endswith('}'):
        return deserialize_obj(s)
    else:
        return deserialize_primitive(s)


def deserialize_list(s: str):
    expressions = split_list(s)
    return [deserialize(i) for i in expressions]


def split_list(s: str) -> list:
    result = []
    s = s[1:-1]
    current_position, expr_start = 0, 0
    while current_position < len(s):
        if s[current_position] == '{' or s[current_position] == '[' or s[current_position] == '"':
            current_position = skip_recursively(s, current_position)
        elif s[current_position] == ',':
            result.append(s[expr_start:current_position])
            current_position += 1
            expr_start = current_position
        else:
            current_position += 1
    if current_position is not expr_start:
        result.append(s[expr_start:])
    return result


def deserialize_obj(s: str):
    result = dict()
    current_position, expr_start = 0, 0
    s = s.strip()
    s = s[1:-1]
    while current_position < len(s):
        if s[current_position] != ',':
            if s[current_position] == '"' or s[current_position] == "'" \
                    or s[current_position] == '[' or s[current_position] == '{':
                current_position = skip_recursively(s, current_position)
            else:
                current_position += 1
        else:
            expr = s[expr_start:current_position].strip()
            field, value = deserialize_expr(expr)
            result[field] = value

            current_position, expr_start = current_position + 1, current_position + 1
    expr = s[expr_start:current_position].strip()
    field, value = deserialize_expr(expr)
    result[field] = value
    return result


def deserialize_expr(s: str) -> (str, str):
    s = s.strip()
    match = re.match(r'"([a-zA-Z_]\w*)"\s*:\s*(.+)', s, re.ASCII)
    if not match:
        raise InvalidJsonException
    field = match.group(1)
    value = deserialize(match.group(2))
    return field, value


def deserialize_primitive(s: str):
    if s.startswith('"') and s.endswith('"'):
        return s[1:-1]
    elif s.isdecimal():
        return int(s)
    elif s.lower() == 'true' or s.lower() == 'false':
        return bool(s)
    elif s.lower() == 'null' or s.lower() == 'undefined':
        return None
    else:
        try:
            return float(s)
        except ValueError:
            raise InvalidJsonException
