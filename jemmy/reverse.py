# -*- coding: utf-8 -*-

from collections import namedtuple
import jemmy.dic  # not strictly required, but documents dependency on dic class
import jemmy.plugins


class Reverse(jemmy.plugins.Plugin):
    """
    Encryption, decryption, and cracking of reversed texts.

    Implements operations encrypt, decrypt and crack.
    """

    def __init__(self, dic):
        self._dic = dic

    def encrypt(self, plaintext, **kwargs):
        return plaintext[::-1]

    def decrypt(self, ciphertext, **kwargs):
        return self.encrypt(plaintext=ciphertext, **kwargs)

    def crack(self, ciphertext, threshold_percent, **kwargs):
        result = namedtuple('Result', ['cracked', 'score', 'plaintext'])
        result.cracked = False
        result.score = 0
        result.plaintext = ''  # must initialize it, as it's just a wrapper object, else it would not properly compare

        potential_plaintext = self.decrypt(ciphertext, **kwargs)

        result.score = self._dic.score(potential_plaintext)
        if result.score >= threshold_percent:
            result.cracked = True
            result.plaintext = self.decrypt(ciphertext, **kwargs)

        return result
