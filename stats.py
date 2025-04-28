def get_word_count(book_content):
    """
    This function takes the text content of a book and returns the word count.
    """
    words = book_content.split()
    return len(words)

def characters_count(book_content):
    """
    This function takes the text content of a book and returns the character count.
    """
    char_dict = {}
    for char in book_content.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1 
    return char_dict


def report_char_count(char_dict):
    """
    This function takes the word count dictoinary and returns a report.
    """
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})

    char_list.sort(key=lambda x: x['count'], reverse=True)
    

    return char_list
