import unittest
from nose.tools import *
import decryptanian.dic


class TestDic(unittest.TestCase):
    def test_empty_dictionary_doesnt_match(self):
        dic = decryptanian.dic.Dic([])
        self.assertFalse(dic.matches('a'))

    def test_dictionary_takes_enumerator_with_values(self):
        dic = decryptanian.dic.Dic(['a'])
        self.assertTrue(dic.matches('a'))

    def test_dictionary_substring_does_not_match(self):
        dic = decryptanian.dic.Dic(['abc'])
        self.assertFalse(dic.matches('a'))
        self.assertFalse(dic.matches('b'))
        self.assertFalse(dic.matches('c'))

    def test_score_of_perfect_match_is_one_of_one(self):
        dic = decryptanian.dic.Dic(['a'])
        self.assertEqual([1, 1], dic.score(['a']))

    def test_score_of_a_half_match(self):
        dic = decryptanian.dic.Dic(['foo', 'bar'])
        self.assertEqual([1, 2], dic.score(['foo', 'baz']))
