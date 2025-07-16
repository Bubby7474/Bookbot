def get_word_count(text):
    word_count = text.split()
    return len(word_count)

def get_character_count(words):
    lower_case = words.lower()
    character_count = {}
    for letter in lower_case:
        if letter not in character_count:
            character_count[letter] = 1
        else:
            character_count[letter] += 1
    print(character_count)



