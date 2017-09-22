# -*- coding: utf-8 -*-

import jemmy.guess_cipher


def test_no_useful_hint_for_empty_ciphertext():
    plugin = jemmy.guess_cipher.GuessCipher(None)
    result = plugin.analyze(ciphertext='', threshold_percent=0)
    assert not result.match
    assert result.score == 0
    assert result.comment == 'For the given threshold 0 "" does not look like hex'


def test_possible_hex_ciphertext():
    plugin = jemmy.guess_cipher.GuessCipher(None)
    ciphertext = '01ab98cd'
    result = plugin.analyze(ciphertext=ciphertext, threshold_percent=50)
    assert result.match
    assert result.score == 50
    assert result.comment == '"{}" might be hex'.format(ciphertext)


def test_perfect_match_hex_ciphertext():
    plugin = jemmy.guess_cipher.GuessCipher(None)
    ciphertext = '0123456789abcdef'
    result = plugin.analyze(ciphertext=ciphertext, threshold_percent=50)
    assert result.match
    assert result.score == 100
    assert result.comment == '{} contains only hex digits and contains all hex digits'.format(ciphertext)
