import application
api = application.api

def test_max():
    args = {'q': "asdjsaklk: which of the following numbers is the largest: 10, 12, 120"}
    assert api(args) == 120

def test_plus():
    args = {'q': "asdjsaklk: what is 5 plus 4"}
    assert api(args) == 9

def test_multiplied():
    args = {'q': "asdjsaklk: what is 5 multiplied 4"}
    assert api(args) == 20

