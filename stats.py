def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_num(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
                chars[lowered] = 1 
    return chars

def chars_sort_on(item):
    return item["num"]


def sort_nums(chars):
    chars_list = []
    for ch, count in chars.items():
         chars_list.append({"char": ch, "num": count})


    chars_list.sort(reverse=True, key=chars_sort_on)
    return chars_list
