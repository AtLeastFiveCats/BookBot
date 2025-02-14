def alpha_check(word_counter, character):
    print("--Begin report of book---")
    print(f"{word_counter} words found in the book")
    dict_list = []
    for key, value in character.items():
        if key.isalpha() == True:
            dictionary = {"key": key, "value": value}
            dict_list.append(dictionary)
    return dict_list

def sort_check(dict_list):
    return dict_list["value"]

def sort_list(alpha_list):
    alpha_list.sort(key=sort_check, reverse=True)
    for item in alpha_list:
        print(f"The '{item["key"]}' character was found {item["value"]} times")
    print("--- End of Report ---")

def character_printer(file_contents):
    character = {}
    for word in file_contents:
        lower_word = word.lower()
        for characters in lower_word:
            if characters not in character:
                character[characters] = 1
            else:
                character[characters] += 1
    return character


def word_count(file_contents):
    word_counter = 0
    split_words = file_contents.split()
    for word in split_words:
        word_counter += 1
    return word_counter



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        total_words = word_count(file_contents)
        total_char = character_printer(file_contents)
        alpha_list = alpha_check(total_words, total_char)
        sort_list(alpha_list)     

main()
