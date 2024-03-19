from hello import more_hello, goodbye


def test_more_hello():
    assert more_hello() == "hi"


def test_goodbye():
    assert goodbye() == "bye"
