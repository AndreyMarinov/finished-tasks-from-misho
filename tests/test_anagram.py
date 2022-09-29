'''Test modul that checks if two strings are anagram'''
import unittest

from src.checking_anagram import is_anagram


class TestAnagram(unittest.TestCase):
    '''Tests for checking if two strings are anagram'''


    def test_anagram(self):
        '''Checking is it anagram'''
        assert is_anagram('hayao','oyaha')


    def test_anagram_one(self):
        '''Checking is it anagram second time'''
        assert is_anagram('emosawe', 'awesome')


    def test_anagram_two(self):
        '''Checking is it anagram third time'''
        assert is_anagram('perfect', 'tfreecp')


    def test_anagram_three(self):
        '''Checking is it anagram forth time'''
        assert is_anagram('desert', 'trsede')


    def test_anagram_if_not(self):
        '''Checking if is not anagram'''
        assert not is_anagram('what', 'tahwae')


if __name__ == "__main__":
    unittest.main()
