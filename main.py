from stats import count_words, count_characters, sorting_dictionary, get_book_text, print_info
import sys

#path_to_frankenstein = "books/frankenstein.txt"
#path_to_shit = "books/shit.txt"

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    number_of_words = count_words(file_contents)
    new_dictionary = count_characters(file_contents)
    new_dictionary = sorting_dictionary(new_dictionary)
    print_info(sys.argv[1], number_of_words, new_dictionary)

main()