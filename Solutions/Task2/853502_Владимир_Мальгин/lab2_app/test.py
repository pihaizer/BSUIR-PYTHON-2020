class TestInternal:
    def __init__(self):
        self.bc = 5

    def __eq__(self, other):
        return self.bc == other.bc


class Test:
    def __init__(self, a: dict):
        self.a = a["a"]
        self.b = a["b"]
        self.abc = a["abc"] if "abc" in a else TestInternal()

    def __eq__(self, other):
        if type(other) is not Test:
            return NotImplemented
        return self.a == other.a and self.b == other.b and self.abc == other.abc


if __name__ == '__main__':
    print(type({"S": "asd"}))

# def open_file(event):
#     file_name = filedialog.Open(root, filetypes=[("*.txt files", ".txt")]).show()
#     if file_name == '':
#         return None
#     if not file_name.endswith(".txt"):
#         file_name += ".txt"
#     global opened_file
#     opened_file = open(file_name)
#
#
# def save_file(event):
#     file_name = filedialog.Open(root, filetypes=[("*.txt files", ".txt")]).show()
#     if file_name == '':
#         return None
#     if not file_name.endswith(".txt"):
#         file_name += ".txt"
#     global save_file
#     save_file = open(file_name, 'w')