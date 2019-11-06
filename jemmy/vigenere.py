# -*- coding: utf-8 -*-

from collections import namedtuple
import jemmy.dic  # not strictly required, but documents dependency on dic class
import jemmy.plugins
import logging


_logger = logging.getLogger(__name__)
_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Vigenere(jemmy.plugins.Plugin):
    """
    Encryption and decryption of vigenere cipher.
    """

    def __init__(self, dic):
        self._dic = dic

    def encrypt(self, plaintext, key, **kwargs):
        return self.__translate(text=plaintext, key=key, factor=1)

    def decrypt(self, ciphertext, key, **kwargs):
        return self.__translate(text=ciphertext, key=key, factor=-1)

    def __translate(self, text, key, factor, **kwargs):
        if not key:
            _logger.fatal("No valid key defined (minimal key length is 1)")
            return None

        translated = []
        key_index = 0
        key = key.upper()
        for symbol in text:
            letter_number = _LETTERS.find(symbol.upper())
            if letter_number == -1:
                translated.append(symbol)  # translate as is, because not a letter
            else:
                letter_number += factor * _LETTERS.find(key[key_index])
                letter_number %= len(_LETTERS)
                translated.append(_LETTERS[letter_number])
                key_index += 1
                key_index %= len(key)

        return ''.join(translated)
