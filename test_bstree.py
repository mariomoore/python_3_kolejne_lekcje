from bstree import *


def test_BSTree_set():
    colors = BSTree()
    colors.set("Cad", "Cad Red")
    assert colors.root.value == "Cad Red"
    colors.set("Cad", "Cadmium Red")
    assert colors.root.key == "Cad"
    assert colors.root.value == "Cadmium Red"
    colors.set("Pthalo", "Pthalo Blue")
    assert colors.root.right.key == "Pthalo"
    colors.set("Aliz", "Alizarin Crimson")
    assert colors.root.left.key == "Aliz"
    return colors


def test_BSTree_get():
    colors = test_BSTree_set()
    assert colors.get("Cad") == "Cadmium Red"
    assert colors.get("Pthalo") == "Pthalo Blue"
    assert colors.get("Aliz") == "Alizarin Crimson"


def test_list():
    colors = test_BSTree_set()
    colors.list()


def test_delete():
    colors = test_BSTree_set()
    colors.set("Gamb", "New Gamboge")
    colors.list()
    assert colors.get("Gamb") == "New Gamboge"
    colors.delete("Pthalo")
    assert colors.get("Pthalo") is None
    assert colors.get("Gamb") == "New Gamboge"
    colors.delete("Aliz")
    assert colors.get("Aliz") is None
    colors.list()

    colors = test_BSTree_set()
    colors.set("Gamb", "New Gamboge")
    colors.set("Prus", "Prussian Blue")
    colors.list()
    colors.delete("Pthalo")
    assert colors.get("Gamb") == "New Gamboge"
    assert colors.get("Prus") == "Prussian Blue"
    colors.delete("Gamb")
    assert colors.get("Gamb") is None
    assert colors.get("Prus")
    colors.delete("Prus")
    assert colors.get("Prus") is None
    colors.delete("Cad")
    assert colors.root.key == "Aliz"
    colors.delete("Aliz")
    assert colors.get("Aliz") is None
    colors.list()


# if __name__ == '__main__':
#     test_delete()
