from stats import count_words, count_characters, sorting_dictionary, get_book_text, print_info

path_to_frankenstein = "books/frankenstein.txt"
path_to_shit = "books/shit.txt"

def main():
    file_contents = get_book_text(path_to_frankenstein)
    number_of_words = count_words(file_contents)
    #print(f"{count_words(file_contents)} words found in the document")
    new_dictionary = count_characters(file_contents)
    new_dictionary = sorting_dictionary(new_dictionary)
    #print(new_dictionary)
    print_info(path_to_frankenstein, number_of_words, new_dictionary)

main()