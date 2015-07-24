# -*- coding: utf-8 -*-


from nose.tools import *
import jemmy.dic
import unittest


class TestDic(unittest.TestCase):
    def test_empty_word_list_raises_exception(self):
        self.assertRaises(jemmy.dic.DicError, lambda: jemmy.dic.Dic([]))

    def test_dictionary_takes_enumerator_with_values(self):
        dic = jemmy.dic.Dic(['a'])
        self.assertTrue(dic.matches('a'))

    def test_dictionary_substring_does_not_match(self):
        dic = jemmy.dic.Dic(['abc'])
        self.assertFalse(dic.matches('a'))
        self.assertFalse(dic.matches('b'))
        self.assertFalse(dic.matches('c'))

    def test_score_of_perfect_match_is_one_of_one(self):
        dic = jemmy.dic.Dic(['a'])
        self.assertEqual(100, dic.score(['a']))

    def test_score_of_a_half_match(self):
        dic = jemmy.dic.Dic(['foo', 'bar'])
        self.assertEqual(50, dic.score(['foo', 'baz']))
