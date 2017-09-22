# -*- coding: utf-8 -*-

from collections import namedtuple
import jemmy.plugins


class GuessCipher(jemmy.plugins.Plugin):
    """
    Tries to guess possible ciphers by analyzing the ciphertext.
    """

    HEX_ALPHABET = '0123456789abcdef'

    def __init__(self, dic):
        self._dic = dic

    def analyze(self, ciphertext, threshold_percent, **kwargs):
        result = namedtuple('Result', ['match', 'score', 'comment'])
        result.match = False
        result.score = 0
        result.comment = 'For the given threshold {} "{}" does not look like hex'.format(threshold_percent, ciphertext)

        alphabet = jemmy.alphabet.Alphabet(ciphertext)

        if alphabet.contains_all(GuessCipher.HEX_ALPHABET) and alphabet.contains_only(GuessCipher.HEX_ALPHABET):
            result.match = True
            result.score = 100
            result.comment = '{} contains only hex digits and contains all hex digits'.format(ciphertext)
        elif alphabet.length() > 0 and alphabet.contains_only(GuessCipher.HEX_ALPHABET):
            result.score = 100 / 16 * alphabet.length()
            result.match = True if result.score >= threshold_percent else False
            result.comment = '"{}" might be hex'.format(ciphertext)
        return result
