def get_word_count(file: str) -> str:
    words = file.split()
    return(f"Found {len(words)} total words")

def get_character_counts(text: str) -> dict[str, int]:
    my_dict = {}
    low_txt = text.lower()
    for char in low_txt:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict

def sort_on(text: tuple[str, int]) -> int:
    return text[1]

def chars_dict_to_sorted_list(my_dict: dict[str, int]) -> list[tuple[str, int]]:
    my_list = []
    for key in my_dict:
        my_list.append((key, my_dict[key]))
    sorted_list = sorted(my_list, reverse=True, key=sort_on)
    return sorted_list

def get_top_words(text: str) -> dict[str, int]:
    my_dict = {}
    split_txt = text.split()
    for word in split_txt:
        word = word.lower()
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    sorted_word = sorted(my_dict.items(), reverse=True, key=lambda x: x[1])
    top_10 = dict(sorted_word[:10])
    return top_10
