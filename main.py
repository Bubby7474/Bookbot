def main():
    import sys
    if len(sys.argv) != 2:
         print ("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    else:
         book_text = sys.argv[1]
    with open(book_text) as f:
        contents = f.read()
    word_count = get_word_count(contents)
    character_count = get_character_count(contents)
    character_list = sorted_list(character_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in character_list:
        char = i["char"]
        count = i["num"]
        if char.isalpha():
            print(f"{char}: {count}")


from stats import get_word_count
from stats import get_character_count
from stats import sorted_list





main()