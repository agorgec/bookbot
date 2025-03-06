def word_count(file_contents):
    return len(file_contents.split())

def char_count(file_contents):
    char_dict = {}
    for char in file_contents.lower():
        if char_dict.get(char):
            char_dict[char] = char_dict[char] + 1

        else:
            char_dict[char] = 1

    return char_dict

def report(word_count, char_dict):
    char_list = sorted(char_dict.items(), key=lambda item: item[1], reverse= True)
    word_count_message = ""
    for char in char_list:
        if char[0].isalpha():
            word_count_message += f"{char[0]}: {char[1]}\n"

    message = f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{word_count_message.strip()}
============= END ===============
"""
    
    return message