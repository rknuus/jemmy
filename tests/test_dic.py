# -*- coding: utf-8 -*-

import jemmy.dic
import pytest


def test_empty_word_list_raises_exception():
    with pytest.raises(jemmy.dic.DicError):
        jemmy.dic.Dic([])


def test_dictionary_takes_enumerator_with_values():
    dic = jemmy.dic.Dic(['a'])
    assert dic.matches('a')


def test_dictionary_substring_does_not_match():
    dic = jemmy.dic.Dic(['abc'])
    assert not dic.matches('a')
    assert not dic.matches('b')
    assert not dic.matches('c')


def test_score_of_perfect_match_is_one_of_one():
    dic = jemmy.dic.Dic(['a'])
    assert dic.score(['a']) == 100


def test_score_of_a_half_match():
    dic = jemmy.dic.Dic(['foo', 'bar'])
    assert dic.score(['foo', 'baz']) == 50
