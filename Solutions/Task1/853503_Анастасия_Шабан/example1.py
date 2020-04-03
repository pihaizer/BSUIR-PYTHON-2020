import re


def word_count(file_name):
    di = {}
    with open(file_name, "r") as file:
        text_string = file.read().lower()
    match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)

    for word in match_pattern:
        count = di.get(word, 0)
        di[word] = count + 1

    di_list = di.keys()

    for words in di_list:
        print(words, di[words])

    print("////////////////////////////////////////////////////////")

    list_d = list(di.items())
    list_d.sort(key=lambda i: i[1], reverse=True)

    for i in list_d:
        print(i[0], ':', i[1])

    print("////////////////////////////////////////////////////////")

    s = "-".join(i[0] for i in list_d[0:10])
    print(s)

