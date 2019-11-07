# -*- coding: utf-8 -*-

import jemmy.reverse


def test_reverse_empty_word():
    plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
    assert plugin.encrypt('') == ''
    assert plugin.decrypt('') == ''


def test_reverse_one_letter_word():
    plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
    assert plugin.encrypt('a') == 'a'
    assert plugin.decrypt('a') == 'a'


def test_reverse_two_letter_word():
    plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
    assert plugin.encrypt('ab') == 'ba'
    assert plugin.decrypt('ab') == 'ba'


def test_reverse_sentence():
    plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
    assert plugin.encrypt('.nohtyP revo ybuR referp I') == 'I prefer Ruby over Python.'
    assert plugin.decrypt('I prefer Ruby over Python.') == '.nohtyP revo ybuR referp I'


def test_crack_empty_word():
    plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
    result = plugin.crack('', threshold_percent=100)
    assert not result.cracked
    assert result.plaintext == ''


def test_crack_single_word_not_in_dic():
    plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
    result = plugin.crack('b', threshold_percent=1)
    assert not result.cracked
    assert result.plaintext == ''


def test_crack_one_of_two_words_in_dic_with_fifty_percent_threshold():
    plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
    result = plugin.crack('b a', threshold_percent=50)
    assert result.cracked
    assert result.plaintext == 'a b'


def test_crack_one_of_two_words_in_dic_with_too_high_threshold():
    plugin = jemmy.reverse.Reverse(jemmy.dic.Dic(['a']))
    result = plugin.crack('b a', threshold_percent=51)
    assert result.cracked
    assert result.plaintext == 'a b'
