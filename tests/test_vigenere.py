# -*- coding: utf-8 -*-

import jemmy.vigenere


def test_translation_fails_for_empty_key():
    plugin = jemmy.vigenere.Vigenere(jemmy.dic.Dic(['a']))
    assert plugin.encrypt(plaintext='', key='') is None
    assert plugin.decrypt(ciphertext='', key='') is None


def test_empty_message_with_caesar_key():
    plugin = jemmy.vigenere.Vigenere(jemmy.dic.Dic(['a']))
    assert plugin.encrypt(plaintext='', key='a') == ''
    assert plugin.decrypt(ciphertext='', key='a') == ''
