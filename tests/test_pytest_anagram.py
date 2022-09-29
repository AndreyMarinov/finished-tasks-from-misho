'''Pytest modul that checks if two strings are anagram'''

from src.checking_anagram import is_anagram

def test_anagram():
    '''Pytest for checking if two strings are anagram'''
    assert is_anagram('hayao', 'oyaha')
