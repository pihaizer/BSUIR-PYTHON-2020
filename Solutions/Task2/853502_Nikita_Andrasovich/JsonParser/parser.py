# Parse any object to/from JSON file
from collections.abc import Sequence


def to_json(obj: object) -> str:
    if is_seq_but_not_str(obj):
        return _seq_to_json_(obj)

    obj_type = str(type(obj).__name__)
    json_str = "{ \"py/object\": \"" + obj_type+"\""

    arguments = obj.__dict__
    for arg in arguments:
        value = arguments[arg]

        if is_not_regular_type(value):
            value = to_json(value)
            json_str += f", \"{arg}\": {value}"
        else:
            value_str = __get_value_str__(value)
            json_str += f", \"{arg}\": {value_str}"

    return json_str + " }"


def _seq_to_json_(obj: Sequence) -> str:
    json_str = "[ "

    for value in obj:
        if is_not_regular_type(value):
            value = to_json(value)
            json_str += f"{value}, "
        else:
            value_str = __get_value_str__(value)
            json_str += f"{value_str}, "

    return rreplace(json_str, ", ", " ]", 1)


def from_json(json_str: str, globals):
    last_attribute_name = None
    obj = None

    while len(json_str):
        first_symbol = json_str[0]
        parsed_symbols_count = 1

        if first_symbol == "{":
            object_end_index = __find_closing_symbol_index__(
                json_str, "}", "{")
            inner_object = from_json(json_str[1:object_end_index], globals)

            if obj == None:
                obj = inner_object
            elif obj != None and last_attribute_name != None:
                setattr(obj, last_attribute_name, inner_object)
                last_attribute_name = None

            parsed_symbols_count += object_end_index
        elif first_symbol == "[":
            collection_end_index = __find_closing_symbol_index__(
                json_str, "]", "[")
            collection = _from_json_collection_(
                json_str[1:collection_end_index], globals)

            if obj == None:
                obj = collection
            else:
                setattr(obj, last_attribute_name, collection)

            parsed_symbols_count += collection_end_index
        elif first_symbol == "\"":
            string_end_index = __find_closing_symbol_index__(
                json_str, "\"", None)
            attribute = json_str[1:string_end_index]

            if last_attribute_name == None:
                last_attribute_name = attribute
            else:
                if last_attribute_name == "py/object":
                    obj = globals[attribute]()
                else:
                    setattr(obj, last_attribute_name, attribute)
                last_attribute_name = None

            parsed_symbols_count += string_end_index
        elif first_symbol == ':' or first_symbol == ' ' or first_symbol == ',':
            pass
        else:
            coma_index = json_str.find(
                ',') if ',' in json_str else len(json_str)
            space_index = json_str.find(
                ' ') if ' ' in json_str else len(json_str)

            attribute_end_index = min(coma_index, space_index)
            attribute_string = json_str[0:attribute_end_index]

            attribute = __get_default_type_arg__(attribute_string)
            setattr(obj, last_attribute_name, attribute)
            last_attribute_name = None

            parsed_symbols_count += attribute_end_index

        json_str = json_str[parsed_symbols_count:]

    return obj


def _from_json_collection_(json_str, globals):
    collection = list()

    while len(json_str):
        first_symbol = json_str[0]
        parsed_symbols_count = 1

        if first_symbol == "{":
            object_end_index = __find_closing_symbol_index__(
                json_str, "}", "{")
            inner_object = from_json(json_str[1:object_end_index], globals)

            collection.append(inner_object)
            parsed_symbols_count += object_end_index
        elif first_symbol == "[":
            collection_end_index = __find_closing_symbol_index__(
                json_str, "]", "[")
            inner_collection = _from_json_collection_(
                json_str[1:collection_end_index], globals)

            collection.append(inner_collection)
            parsed_symbols_count += collection_end_index
        elif first_symbol == "\"":
            string_end_index = __find_closing_symbol_index__(
                json_str, "\"", None)
            attribute = json_str[1:string_end_index]

            collection.append(attribute)
            parsed_symbols_count += string_end_index
        elif first_symbol == ':' or first_symbol == ' ' or first_symbol == ',':
            pass
        else:
            coma_index = json_str.find(
                ',') if ',' in json_str else len(json_str)
            space_index = json_str.find(
                ' ') if ' ' in json_str else len(json_str)

            attribute_end_index = min(coma_index, space_index)
            attribute_string = json_str[0:attribute_end_index]

            attribute = __get_default_type_arg__(attribute_string)

            collection.append(attribute)
            parsed_symbols_count += attribute_end_index

        json_str = json_str[parsed_symbols_count:]

    return collection


def __get_value_str__(value) -> str:
    if value == None:
        return "null"
    elif isinstance(value, str):
        return f"\"{__replace_escaped_symbols__(str(value))}\""
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)


def __get_default_type_arg__(arg_string: str):
    if arg_string == "false":
        return False
    elif arg_string == "true":
        return True
    elif arg_string == "null":
        return None
    elif arg_string.isnumeric():
        return int(arg_string)
    else:
        return float(arg_string)


def __find_closing_symbol_index__(string: str, symbol: chr, reverseSymbol: chr):
    depth = 0

    for i in range(1, len(string)):
        if string[i] == reverseSymbol and string[i-1] != "\\":
            depth += 1
        elif string[i] == symbol and string[i-1] != "\\":
            if depth == 0:
                return i
            else:
                depth -= 1
    else:
        return -1


def __replace_escaped_symbols__(string: str) -> str:
    string = string.replace("}", r"\}")
    return string.replace("{", r"\{")


def is_not_regular_type(obj: object) -> bool:
    return hasattr(obj, "__dict__") or is_seq_but_not_str(obj)


def is_seq_but_not_str(obj) -> bool:
    return isinstance(obj, Sequence) and not isinstance(obj, (str, bytes, bytearray))


def rreplace(string, old, new, occurrence):
    li = string.rsplit(old, occurrence)
    return new.join(li)
