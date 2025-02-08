def main():

    book = "books/frankenstein.txt"
    file_contents = get_text(book)
    num_words = word_count(file_contents)
    num_chars = char_count(file_contents)
    char_list = get_sorted_char_nums(num_chars)
    
    
    print(f"Report for {book}:")
    print(f"Word count: {num_words}")
    for i in char_list:
        print(f"'{i["char"]}' is found {i["num"]} times")

    return

def get_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    count = len(words)
    return count

def char_count(text):
    chars = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def sort_on(dict):
    return dict["num"]

def get_sorted_char_nums(dict):
    char_list = []

    for i in dict:
        if i.isalpha():
            char_list.append({"char":i, "num":dict[i]})
            char_list.sort(reverse=True, key=sort_on)

    return char_list


main()
    
    
