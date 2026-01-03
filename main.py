from stats import get_num_words, get_character_num

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_character_num(text)
    print(f"Found {num_words} total words")
    print(chars_dict)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()



main()