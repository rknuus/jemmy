from collections import namedtuple
from nose.tools import *
import jemmy.reverse
import unittest


class TestReverse(unittest.TestCase):
    def test_reverse_empty_word(self):
        plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
        self.assertEqual(plugin.decrypt(''), '')

    def test_reverse_one_letter_word(self):
        plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
        self.assertEqual(plugin.decrypt('a'), 'a')

    def test_reverse_two_letter_word(self):
        plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
        self.assertEqual(plugin.decrypt('ab'), 'ba')

    def test_reverse_sentence(self):
        plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
        self.assertEqual(plugin.decrypt('I prefer Ruby over Python.'), '.nohtyP revo ybuR referp I')

    def test_crack_empty_word(self):
        plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
        result = plugin.crack('', threshold_percent=100)
        self.assertTrue(result.cracked)
        self.assertEqual(result.plaintext, '')

    def test_crack_single_word_not_in_dic(self):
        plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
        result = plugin.crack('b', threshold_percent=1)
        self.assertFalse(result.cracked)
        self.assertEqual(result.plaintext, '')

    def test_crack_one_of_two_words_in_dic_with_fifty_percent_threshold(self):
        plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
        result = plugin.crack('b a', threshold_percent=50)
        self.assertTrue(result.cracked)
        self.assertEqual(result.plaintext, 'a b')

    def test_crack_one_of_two_words_in_dic_with_too_high_threshold(self):
        plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
        result = plugin.crack('b a', threshold_percent=51)
        self.assertTrue(result.cracked)
        self.assertEqual(result.plaintext, 'a b')
