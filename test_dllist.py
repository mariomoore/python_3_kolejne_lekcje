from dllist import *


def test_push():
    colors = DoubleLinkedList()
    colors.push("Błękit flatocyjaninowy")
    assert colors.count() == 1
    colors.push("Błękit ultramarynowy")
    assert colors.count() == 2


def test_pop():
    colors = DoubleLinkedList()
    colors.push("Magenta")
    colors.push("Alizaryna")
    colors.push("Brunat Van Dycka")
    assert colors.pop() == "Brunat Van Dycka"
    assert colors.get(1) == "Alizaryna"
    assert colors.pop() == "Alizaryna"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None


def test_unshift():
    colors = DoubleLinkedList()
    colors.push("Zieleń Guigneta")
    colors.push("Zieleń soczysta")
    colors.push("Brunat Van Dycka")
    assert colors.unshift() == "Zieleń Guigneta"
    assert colors.unshift() == "Zieleń soczysta"
    assert colors.unshift() == "Brunat Van Dycka"
    assert colors.unshift() == None


def test_shift():
    colors = DoubleLinkedList()
    colors.shift("Pomarańcz kadmowy")
    assert colors.count() == 1

    colors.shift("Fiolet karbazolowy")
    assert colors.count() == 2

    assert colors.pop() == "Pomarańcz kadmowy"
    assert colors.count() == 1
    assert colors.pop() == "Fiolet karbazolowy"
    assert colors.count() == 0


def test_remove():
    colors = DoubleLinkedList()
    colors.push("Kobaltowy")
    colors.push("Biel cynkowa")
    colors.push("Żółć niklowa")
    colors.push("Perinone")
    assert colors.remove("Kobaltowy") == 0
    colors.dump("przed perinone")
    assert colors.remove("Perinone") == 2
    colors.dump("po perinone")
    assert colors.remove("Żółć niklowa") == 1
    assert colors.remove("Biel cynkowa") == 0


def test_first():
    colors = DoubleLinkedList()
    colors.push("Czerwień kadmowa")
    assert colors.first() == "Czerwień kadmowa"
    colors.push("Żółć arylidowa")
    assert colors.first() == "Czerwień kadmowa"
    colors.shift("Zieleń flatocyjaminowa")
    assert colors.first() == "Zieleń flatocyjaminowa"


def test_last():
    colors = DoubleLinkedList()
    colors.push("Czerwień kadmowa")
    assert colors.last() == "Czerwień kadmowa"
    colors.push("Żółć arylidowa")
    assert colors.last() == "Żółć arylidowa"
    colors.shift("Zieleń flatocyjaminowa")
    assert colors.last() == "Żółć arylidowa"


def test_get():
    colors = DoubleLinkedList()
    colors.push("Cynober")
    assert colors.get(0) == "Cynober"
    colors.push("Zieleń soczysta")
    assert colors.get(0) == "Cynober"
    assert colors.get(1) == "Zieleń soczysta"
    colors.push("Żółć kadmowa")
    assert colors.get(0) == "Cynober"
    assert colors.get(1) == "Zieleń soczysta"
    assert colors.get(2) == "Żółć kadmowa"
    assert colors.pop() == "Żółć kadmowa"
    assert colors.get(0) == "Cynober"
    assert colors.get(1) == "Zieleń soczysta"
    assert colors.get(2) == None
    colors.pop()
    assert colors.get(0) == "Cynober"
    colors.pop()
    assert colors.get(0) == None
