def get_word_count(text):
    word_count = text.split()
    return len(word_count)

character_count = {}

def get_character_count(words):
    lower_case = words.lower()
    for letter in lower_case:
        if letter not in character_count:
            character_count[letter] = 1
        else:
            character_count[letter] += 1

def sorted_list(characters):
    unsorted = character_count.items()
    sorted_tuples = (sorted(unsorted, key= lambda item: item[1], reverse=True))
    sorted_list = []
    for char, count in sorted_tuples:
        sorted_list.append({"char": char, "num": count})
    return (sorted_list)


#Keep below because it kinda works, but not correctly
#Can potentially be modified to work, but for now
#Work on above
#def get_character_list(characters):
    #character_list = character_count.items()
    #new_list = sorted(character_list, reverse=True, key=lambda pair: pair[1])
    #return (new_list)