def get_book_text(filepath):
    file_path = filepath
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    count = text.split()
    return len(count)

def main():
    book_text = get_book_text("workspace/bootdotdev/bookbot/books/frankenstein.txt")
    # Above relative path (workspace/bootdotdev/bookbot/books/frankenstein.txt) works for VSCode
    # However, for it to work in WSL, it needs to be (books/frankenstein.txt)
    word_count = get_word_count(book_text)
    print(f"{word_count} words were found in this document")
main()