import sys
from stats import get_word_count
from stats import get_character_counts
from stats import chars_dict_to_sorted_list

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path: str, word_count: str, sorted_list: list[tuple[str, int]]) -> None:
    print("            <BookBot>            ")
    print(" ")
    print(f"📖 Reading: {book_path} ...")
    print(" ")
    print(f"📊 Total Words: {word_count}")
    print(" ")
    print(f"<📚 Character Count>")
    for char, count in sorted_list:
        if char.isalpha():
            print(f" {char}: {count}")
    print(" ")
    print("-------------End!-------------")





def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_character_counts(text)
    sorted_list = chars_dict_to_sorted_list(char_count)
    print_report(book_path, word_count, sorted_list)


main()
