'''Modul that checks if two strings are anagram or not'''


def is_anagram(first_word, second_word):
    '''Check if first_word is equal to second_word and return it'''
    return sorted(first_word) == sorted(second_word)


is_anagram('haoya', 'ahoya')
