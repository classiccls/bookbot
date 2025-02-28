def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(text_to_count):
    table_to_count = text_to_count.split()
    return len(table_to_count)

def count_characters(text_to_count):
    list_to_count = list(text_to_count.lower())
    dictionary_of_letters = {}
    for letter in list_to_count:
        if letter in dictionary_of_letters:
            dictionary_of_letters[letter] += 1
        else:
            dictionary_of_letters[letter] = 1
    return dictionary_of_letters

def sorting_dictionary(dictionary_to_sort):
    sorted_list = sorted(dictionary_to_sort.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_list)

def print_info(path_to_file, number_of_characters, dictionary_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_characters} total words")
    print("--------- Character Count -------")
    for word in dictionary_sorted:
        if word.isalpha():
            print(f"{word}: {dictionary_sorted[word]}")
    print("============= END ===============")