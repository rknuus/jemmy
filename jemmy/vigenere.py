# -*- coding: utf-8 -*-

from collections import namedtuple
import jemmy.dic  # not strictly required, but documents dependency on dic class
import jemmy.plugins
import logging


_logger = logging.getLogger(__name__)


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Vigenere(jemmy.plugins.Plugin):
    """
    Encryption and decryption of vigenere cipher.
    """

    def __init__(self, dic):
        self._dic = dic

    def encrypt(self, plaintext, key, **kwargs):
        if not key:
            _logger.fatal("No valid key defined (minimal key length is 1)")
            return None

        translated = []
        key_index = 0
        key = key.upper()
        for symbol in plaintext:
            letter_number = LETTERS.find(symbol.upper())
            if letter_number == -1:
                translated.append(symbol)  # translate as is, because not a letter
            else:
                letter_number += LETTERS.find(key[key_index])
                letter_number %= len(LETTERS)
                translated.append(LETTERS[letter_number])
                key_index += 1
                key_index %= len(key)

        return ''.join(translated)

    def decrypt(self, ciphertext, **kwargs):
        return ciphertext

    def crack(self, ciphertext, threshold_percent, **kwargs):
        result = namedtuple('Result', ['cracked', 'score', 'plaintext'])
        result.cracked = False
        result.score = 0
        result.plaintext = ''  # must initialize it, as it's just a wrapper object, else it would not properly compare

        return result
