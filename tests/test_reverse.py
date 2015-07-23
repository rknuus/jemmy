import unittest
from nose.tools import *
import decryptanian.reverse


class TestReverse(unittest.TestCase):
    def test_reverse_empty_word(self):
        r = decryptanian.reverse.Reverse()
        self.assertEqual(r.decrypt(''), '')

    def test_reverse_one_letter_word(self):
        r = decryptanian.reverse.Reverse()
        self.assertEqual(r.decrypt('a'), 'a')

    def test_reverse_two_letter_word(self):
        r = decryptanian.reverse.Reverse()
        self.assertEqual(r.decrypt('ab'), 'ba')

    def test_reverse_two_letter_word(self):
        r = decryptanian.reverse.Reverse()
        self.assertEqual(r.decrypt('I prefer Ruby over Python.'), '.nohtyP revo ybuR referp I')
