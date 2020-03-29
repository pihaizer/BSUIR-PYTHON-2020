import random


def generate_random_sentence(words: list) -> str:
    result: str = ""
    shuffled_words = words.copy()
    random.shuffle(shuffled_words)
    for word in shuffled_words:
        result += word + ' '
    result = result.capitalize()
    result = result.strip()
    result += '.'
    return result


def main():
    words = ["one", "two", "three"]
    print(generate_random_sentence(words))


if __name__ == "__main__":
    main()
