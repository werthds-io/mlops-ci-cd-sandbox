from hello import more_hello, goodbye, add


def test_more_hello():
    assert more_hello() == "hi"


def test_goodbye():
    assert goodbye() == "bye"


def test_add():
    assert add(1, 1) == 2
