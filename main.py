def get_book_text(filepath):
    file_path = filepath
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
def main():
    book_text = get_book_text("workspace/bootdotdev/bookbot/books/frankenstein.txt")
    print(book_text)
main()