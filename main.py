import sys
from stats import (
    get_num_words,
      get_character_num,
        sort_nums,
        )

if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_character_num(text)
    sort_numbers = sort_nums(chars_dict)
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort_numbers:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()



main()