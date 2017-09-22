# -*- coding: utf-8 -*-

import jemmy.alphabet


def test_alphabet_size_of_empty_text_is_zero():
    alphabet = jemmy.alphabet.Alphabet('')
    assert alphabet.length() == 0


def test_alphabet_size_of_one_letter_text_is_one():
    alphabet = jemmy.alphabet.Alphabet('a')
    assert alphabet.length() == 1


def test_alphabet_size_of_mono_letter_text_is_one():
    alphabet = jemmy.alphabet.Alphabet('aa')
    assert alphabet.length() == 1


def test_alphabet_size_of_dual_letter_text_is_two():
    alphabet = jemmy.alphabet.Alphabet('ab')
    assert alphabet.length() == 2
