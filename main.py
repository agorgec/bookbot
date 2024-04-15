def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    header()
    print(f"Number of words: {num_words}")
    chars_dict = get_chars_dict(text)
    chars_sorted = chars_dict_to_sorted_list(chars_dict)

    for item in chars_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']} character was found {item['num']} times")

    end()


def header():
    print("--- Begin report of books/frankenstein.txt ---")


def end():
    print("--- End report of books/frankenstein.txt ---")


def sort_on(d):
    return d["num"]


def get_num_words(text):
    words = text.split()
    return len(words)


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
