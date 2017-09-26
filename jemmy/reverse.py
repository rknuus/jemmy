# -*- coding: utf-8 -*-

from collections import namedtuple
import jemmy.dic  # not strictly required, but documents dependency on dic class
import jemmy.plugins


class Reverse(jemmy.plugins.Plugin):
    """
    Decryption and cracking of reversed texts.

    Implements operations decrypt and crack.
    """

    def __init__(self, dic):
        self._dic = dic

    def decrypt(self, ciphertext, **kwargs):
        return ciphertext[::-1]

    def crack(self, ciphertext, threshold_percent, **kwargs):
        result = namedtuple('Result', 'cracked plaintext')
        result.cracked = False
        result.plaintext = ''  # must initialize it, as it's just a wrapper object, else it would not properly compare

        if not ciphertext:
            result.cracked = True
            result.plaintext = ciphertext  # rubbish in, rubbish out
            return result

        potential_plaintext = self.decrypt(ciphertext, **kwargs)

        if self._dic.score(potential_plaintext) >= threshold_percent:
            result.cracked = True
            result.plaintext = self.decrypt(ciphertext, **kwargs)

        return result
