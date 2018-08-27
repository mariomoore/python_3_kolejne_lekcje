from suffixarray import *


def test_suffixarray():
    sarray = Suffixarray('cba')
    assert sarray.word_sa_sorted[0] == 'a'
    assert sarray.word_sa_sorted[1] == 'ba'
    assert sarray.word_sa_sorted[2] == 'cba'


def test_finding_shortest():
    sarray = Suffixarray('abrakadabra')
    assert sarray.find_shortest('abra') == 'abra'
    assert sarray.find_shortest('xxx') is None


def test_finding_longest():
    sarray = Suffixarray('abrakadabra')
    assert sarray.find_longest('abra') == 'abrakadabra'
    assert sarray.find_longest('xxx') is None


def test_finding_all():
    sarray = Suffixarray('abrakadabra')
    all_values = sarray.find_all('abra')
    assert all_values[0] == 'abra'
    assert all_values[1] == 'abrakadabra'
    all_values = sarray.find_all('ra')
    assert all_values[0] == 'ra'
    assert all_values[1] == 'rakadabra'
    assert sarray.find_all('xxx') is None
