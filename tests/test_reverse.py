from collections import namedtuple
from nose.tools import *
import jemmy.reverse
import unittest


class TestReverse(unittest.TestCase):
    def test_reverse_empty_word(self):
        plugin = jemmy.reverse.Reverse()
        self.assertEqual(plugin.decrypt(''), '')

    def test_reverse_one_letter_word(self):
        plugin = jemmy.reverse.Reverse()
        self.assertEqual(plugin.decrypt('a'), 'a')

    def test_reverse_two_letter_word(self):
        plugin = jemmy.reverse.Reverse()
        self.assertEqual(plugin.decrypt('ab'), 'ba')

    def test_reverse_sentence(self):
        plugin = jemmy.reverse.Reverse()
        self.assertEqual(plugin.decrypt('I prefer Ruby over Python.'), '.nohtyP revo ybuR referp I')

    def test_crack_empty_word(self):
        plugin = jemmy.reverse.Reverse()
        result = plugin.crack('')
        self.assertEqual(result.cracked, True)
        self.assertEqual(result.plaintext, '')

    def test_crack_two_letter_word(self):
        plugin = jemmy.reverse.Reverse()
        result = plugin.crack('ba')
        self.assertEqual(result.cracked, True)
        self.assertEqual(result.plaintext, 'ab')
