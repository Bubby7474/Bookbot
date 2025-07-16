def main():
    book_text = get_book_text("books/frankenstein.txt")
    # Above relative path (workspace/bootdotdev/bookbot/books/frankenstein.txt) works for VSCode
    # However, for it to work in WSL, it needs to be (books/frankenstein.txt)
    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import get_word_count


main()