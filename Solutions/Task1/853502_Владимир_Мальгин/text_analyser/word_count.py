def count_words(text: str) -> dict:
    punctuation_marks = ",.?!:()\'\""
    for char in punctuation_marks:
        text = text.replace(char, ' ')
    words = text.lower().split()
    words_dict = dict()
    for w in words:
        if w in words_dict.keys():
            words_dict[w] += 1
        else:
            words_dict[w] = 1
    return words_dict


def count_words_sorted(text: str) -> dict:
    words_dict = count_words(text)
    sorted_words = dict({k: v for k, v in sorted(words_dict.items(), key=lambda kv: kv[1], reverse=True)})
    return sorted_words


def get_text_from_file(file_path: str) -> str:
    with open(file_path) as file:
        result = file.read()
    return result


def main():
    text = get_text_from_file("../files/text.txt")
    words_dict = count_words(text)
    sorted_words = dict({k: v for k, v in sorted(words_dict.items(), key=lambda kv: kv[1], reverse=True)})
    print(sorted_words)


if __name__ == "__main__":
    main()
