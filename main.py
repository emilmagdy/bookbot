import sys
from stats import get_word_count, characters_count, report_char_count


def get_book_text(book):
    """
    This function takes a book object and returns its text content.
    """
    with open(book) as f:
        book_content = f.read()

    return book_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_content = get_book_text(book)
    word_count = get_word_count(book_content)
    char_count = characters_count(book_content)
    char_list = report_char_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found in {book}")
    print("----------- Word Count -------------")

    print(f"Found {word_count} total words")
    print("----------- Character Count -------------")

    for char in char_list:
        print(f"{char['char']}: {char['count']}")


main()

