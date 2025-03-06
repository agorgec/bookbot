import sys
from stats import word_count, char_count, report


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_contents = get_book_text(sys.argv[1])
        number_of_words = word_count(file_contents)
        char_dict = char_count(file_contents)
        print(report(number_of_words, char_dict))


main()