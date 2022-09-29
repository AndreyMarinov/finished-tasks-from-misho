'''Modul that checks if two strings are anagram or not'''


def is_anagram(first_word:str, second_word:str) -> bool:
    '''Check if first_word is equal to second_word and return it

    :param: first_word:    str first word to compare with the second
    :param: second_word:   str second word to compare with the first
    :return: bool if first word is anagram of second word.
    '''
    return sorted(first_word) == sorted(second_word)
