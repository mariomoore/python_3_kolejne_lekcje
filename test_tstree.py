from tstree import *


def test_TSTree_set_get():
    tree = TSTree()
    tree.set('apple', 5)
    tree.set('application', 11)
    tree.set('winner', 6)
    tree.set('loser', 5)
    tree.set('win', 3)
    assert tree.get('apple') == 5
    assert tree.get('application') == 11
    assert tree.get('winner') == 6
    assert tree.get('loser') == 5
    assert tree.get('win') == 3
    assert tree.get('x') is None
    return tree


def test_TSTree_find_shortest():
    tree = test_TSTree_set_get()
    assert tree.find_shortest('appl') == {'apple': 5}
    assert tree.find_shortest('wi') == {'win': 3}
    assert tree.find_shortest('x') is None


def test_TSTree_find_longest():
    tree = test_TSTree_set_get()
    assert tree.find_longest('appl') == {'application': 11}
    assert tree.find_longest('wi') == {'winner': 6}
    assert tree.find_longest('x') is None


def test_TSTree_find_part():
    tree = test_TSTree_set_get()
    assert tree.find_part('applic') == {'apple': 5}
    assert tree.find_part('winn') == {'win': 3}
    assert tree.find_part('x') is None
