from .exceptions import InvalidJsonException


def skip_recursively(s: str, position: int) -> int:
    try:
        current_symbol = s[position]
    except InvalidJsonException:
        raise InvalidJsonException
    looking_for_symbol = ''
    if current_symbol == '{':
        looking_for_symbol = '}'
    elif current_symbol == '[':
        looking_for_symbol = ']'
    elif current_symbol == "\"" or current_symbol == "\'":
        return skip_str(s, position)

    new_position = position + 1
    try:
        while s[new_position] is not looking_for_symbol:
            if s[new_position] == '{' or s[new_position] == '[' or s[new_position] == '"':
                new_position = skip_recursively(s, new_position)
            else:
                new_position += 1
    except IndexError:
        raise InvalidJsonException
    return new_position + 1


def skip_str(s: str, position: int) -> int:
    current_symbol = s[position]
    position += 1
    position += symbols_before_char(s, current_symbol, position) + 1
    return position


def symbols_before_char(s: str, symbol: str, position: int):
    count = 0
    try:
        if s[position] is symbol:
            return count
        count, position = count + 1, position + 1
        while s[position] != symbol or s[position - 1] == '\\':
            count, position = count + 1, position + 1
    except IndexError:
        raise InvalidJsonException
    return count
