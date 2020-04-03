import json


def obj_dict(obj):
    fields = dict()
    fields.update(obj.__class__.__dict__)
    fields.update(obj.__dict__)
    fields = dict(filter(lambda x: not x[0].startswith('_'), fields.items()))
    new_fields = dict()
    for k, v in fields.items():
        if hasattr(v, '__dict__'):
            v = obj_dict(v)
        new_fields[k] = v
    return new_fields


def dumps(arg):
    if isinstance(arg, (int, float)):
        return str(arg)
    if isinstance(arg, type(None)):
        return 'null'
    if isinstance(arg, str):
        return '\"' + arg.replace('\'', '\"') + '\"'
    if isinstance(arg, (tuple, list)):
        return '[' + ', '.join([dumps(c_i) for c_i in arg]) + ']'
    if isinstance(arg, dict):
        dict_keys = arg.keys()
        if not all([isinstance(k, (str, float, int)) for k in dict_keys]):
            raise TypeError("keys must be a string or a number")

        keys = []
        for key in list(dict_keys):
            if isinstance(key, (int, float)):
                keys.append(str(key))
            else:
                keys.append(key)

        values = arg.values()
        return '{' + ', '.join(['{}: {}'.format(dumps(k), dumps(v))
                                    for k, v in sorted(zip(keys, values), key=lambda x: str(x[0]))]) + '}'

def loads(json_str):

    def next_symbol(ind):
        for i in range(ind, len(json_str)):
            if json_str[i] not in " \t\n\r":
                ind = i
                break
        if ind == len(json_str):
            return ind, "end"
        symb = json_str[ind]
        if symb == '{' or symb == '}' or symb == '[' or symb == ']' or symb == ',' or symb == ':':
            return ind + 1, symb
        elif symb == '"':
            return ind + 1, "str"
        elif symb in "-0123456789.":
            return ind + 1, "numb"

        stay = len(json_str) - ind
        if stay >= 5 and json_str[ind:ind + 5].lower() == 'false':
            return ind + 5, "false"
        if stay >= 4 and json_str[ind:ind + 4].lower() == 'true':
            return ind + 4, "true"
        if stay >= 4 and json_str[ind:ind + 4].lower() == 'null':
            return ind + 4, "null"
        return ind, "end"

    def numb_decode(index, flag):
        for i in range(index, len(json_str)):
            if json_str[i] not in " \t\n\r":
                index = i
                break

        end_index = index
        end = False
        while end_index < len(json_str):
            if json_str[end_index] not in "-+0123456789.eE":
                end_of_numb = end_index - 1
                end = True
                break
            else:
                end_index += 1
        if not end:
            end_of_numb = end_index - 1

        try:
            number = int(json_str[index:end_of_numb + 1])
        except ValueError:
            number = None
            pass
        if number is not None:
            flag = True
        else:
            try:
                flag = True
                number = float(json_str[index:end_of_numb + 1])
            except ValueError:
                flag = False
        return end_of_numb + 1, flag, number

    def str_decode(ind, flag):
        str = ''
        for i in range(ind, len(json_str)):
            if json_str[i] not in " \t\n\r":
                ind = i
                break
        symb = json_str[ind]
        end_str = False
        ind += 1
        while not end_str:
            if ind == len(json_str):
                break
            symb = json_str[ind]
            if symb == '"':
                end_str = True
                ind += 1
                break
            else:
                ind += 1
                str += symb

        return ind, flag, str

    def list_decode(ind, flag):
        recode_list = []
        ind, next_symb = next_symbol(ind)
        not_end = False
        while not not_end:
            next_index, next_symb = next_symbol(ind)
            if next_symb == ",":
                ind, next_symb = next_symbol(ind)
            elif next_symb == "]":
                ind, next_symb = next_symbol(ind)
                break
            else:
                ind, flag, element = object_decode(ind, flag)
                if not flag:
                    return ind, flag, None
                recode_list.append(element)
        return ind, flag, recode_list

    def dict_decode(index, flag):
        obj = {}
        index, next_symb = next_symbol(index)
        not_end = False
        while not not_end:
            next_index, next_symb = next_symbol(index)
            if next_symb == "end":
                flag = False
                return index, flag, None
            elif next_symb == ",":
                index, next_symb = next_symbol(index)
            elif next_symb == "}":
                index, next_symb = next_symbol(index)
                return index, flag, obj
            else:
                index, flag, key = str_decode(index, flag)
                if not flag:
                    return index, flag, None
                index, next_symb = next_symbol(index)
                if next_symb != ":":
                    flag = False
                    return index, flag, None
                index, flag, value = object_decode(index, flag)
                if not flag:
                    return index, flag, None
                obj[key] = value

    def object_decode(index, flag):
        next_index, first_element = next_symbol(index)
        if first_element == "[":
            return list_decode(index, flag)
        elif first_element == "{":
            return dict_decode(index, flag)
        elif first_element == "numb":
            return numb_decode(index, flag)
        elif first_element == "str":
            return str_decode(index, flag)
        elif first_element == "true":
            index, first_element = next_symbol(index)
            return index, flag, True
        elif first_element == "false":
            index, first_element = next_symbol(index)
            return index, flag, False
        elif first_element == "null":
            index, first_element = next_symbol(index)
            return index, flag, None
        else:
            raise ValueError('Invalid input')

        return obj, index, flag

    obj = object_decode(0, True)[2]
    return obj


class JsonConverter:

    @classmethod
    def my_dumps(cls, arg):
        return dumps(arg)

    @classmethod
    def my_loads(cls, arg):
        return loads(arg)


class a:
    def __init__(self, arg, name, bil = True):
        self.number = arg;
        self.Name = name;
        self.trak = bil


if __name__ == '__main__':

    b = a(5, 'maks')
    json_data = json.dumps(obj_dict(b))
    json_data2 = JsonConverter.my_dumps(obj_dict(b))
    print(json_data)
    print(json_data2)
    print(json.loads(json_data))
    print(JsonConverter.my_loads(json_data2))

    data = [1, 2, 3.4]
    json_data = json.dumps(data)
    json_data2 = JsonConverter.my_dumps(data)
    print(json_data)
    print(json.loads(json_data2))
    print(JsonConverter.my_loads(json_data))

    data = ('1', 2, 3.3, (4,), None, 56)
    json_data = json.dumps(data)
    json_data2 = JsonConverter.my_dumps(data)
    print(json.loads(json_data2))
    print(JsonConverter.my_loads(json_data))
