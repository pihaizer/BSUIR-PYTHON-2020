import inspect

from .utility import skip_str


def serialize(obj) -> str:
    obj_type = type(obj)
    result = ''
    if obj is None:
        result = "null"
    elif is_primitive(obj):
        result = '{value}'.format(value=str(obj))
        if obj_type is str:
            result = result.replace('"', r'\"')
            result = '"' + result + '"'
        if obj_type is bool:
            result = result.lower()
    elif obj_type == list:
        result += '['
        for element in obj:
            result += serialize(element)
            result += ','
        result = result[:-1]
        result += ']'
    elif obj_type == dict:
        result += serialize_dict(obj)
    else:
        result = serialize_object(obj)
    return result


def serialize_dict(obj):
    result = '{'
    for key, value in obj.items():
        result += serialize(str(key)) + ':' + serialize(value) + ','
    result = result[:-1] + '}'  # remove last ','
    return result


def serialize_pretty(obj) -> str:
    s = serialize(obj)
    current_position = 0
    current_intend = 0

    def insert_newline(string, position) -> str:
        string = string[:position] + \
                 "\n" + \
                 "    " * current_intend + \
                 string[position:]
        return string

    while current_position < len(s):
        if s[current_position] == "\"" or s[current_position] == "\'":
            current_position = skip_str(s, current_position)
        if s[current_position] == '{' or s[current_position] == '[':
            current_intend += 1
            s = insert_newline(s, current_position + 1)
            current_position += 4 * current_intend + 1
        elif s[current_position] == '}' or s[current_position] == ']':
            current_intend -= 1
            s = insert_newline(s, current_position)
            current_position += 4 * current_intend + 1
        elif s[current_position] == ',':
            s = insert_newline(s, current_position + 1)
            current_position += 4 * current_intend + 1
        elif s[current_position] == ':':
            s = s[:current_position + 1] + ' ' + s[current_position + 1:]
            current_position += 1

        current_position += 1

    return s.strip()


def serialize_object(obj) -> str:
    d = {k: getattr(obj, k, '') for k in obj.__dir__() if
         k[:2] != '__' and type(getattr(obj, k, '')).__name__ != 'method'}
    result = '{'
    for field in d:
        result += '"{field}":{value},'.format(field=field, value=serialize(d[field]))
    result = result[:-1] + '}' if len(d) > 0 else result + '}'
    return result


def is_primitive(value):
    primitives = (bool, int, float, str, None)
    return type(value) in primitives
