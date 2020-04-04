import inspect
import re

class JsonFormatError(Exception):
    pass

def to_json(obj):
    if isinstance(obj, list) or isinstance(obj, tuple):
        json_string = '['
        for (i, value) in enumerate(obj):
            json_string += f'{to_json(value)}'
            if i < len(obj) - 1:
                json_string += ', '
        json_string += ']'
        return json_string
    elif isinstance(obj, dict):
        json_string = '{'
        for i, (key, value) in enumerate(obj.items()):
            converted_value = to_json(value)
            json_string += f'"{key}": {converted_value}'
            if i < len(obj) - 1:
                json_string += ', '
        json_string += '}'
        return json_string
    elif isinstance(obj, str) or isinstance(obj, bool) or isinstance(obj, int):
        represent_str = repr(obj)
        represent_str = represent_str.replace("'", '"')
        represent_str = represent_str.replace('True', 'true')
        represent_str = represent_str.replace('False', 'false')
        return represent_str
    else:
        attributes = inspect.getmembers(type(obj), lambda x: not inspect.isroutine(x))
        attributes = [x for x in attributes if not (x[0].startswith('__') and x[0].endswith('__'))]
        json_string = '{'
        for i, (key, value) in enumerate(attributes):
            converted_value = to_json(value)
            json_string += f'"{key}": {converted_value}'
            if i < len(attributes) - 1:
                json_string += ', '
        json_string += '}'
        return json_string

def from_json(json_string):
    json_general_pattern = re.compile(r"^({|\[)[^()']*(}|\])$")
    json_key_antipattern = re.compile('[^"]:')
    json_bool_antipattern = re.compile('(True|False)')
    try:
        if re.match(json_general_pattern, json_string) and not (re.search(json_key_antipattern, json_string) or re.search(json_bool_antipattern, json_string)):
            json_string = json_string.replace('true', 'True')
            json_string = json_string.replace('false', 'False')
            return eval(json_string)
        else:
            raise JsonFormatError
    except SyntaxError:
        raise JsonFormatError