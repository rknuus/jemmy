# -*- coding: utf-8 -*-


class Alphabet:
    def __init__(self, text):
        self._set = set(text.lower())

    def length(self):
        return len(self._set)

    def contains_all(self, alphabet):
        return self._set.issuperset(set(alphabet.lower()))

    def contains_only(self, alphabet):
        return self._set.issubset(set(alphabet.lower()))
