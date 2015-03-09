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

def test_square_and_cube():
    args = {'q': "asdjsaklk: which of the following numbers is both a square and a cube: 68, 1"}
    assert api(args) == 1

def test_paris():
    args = {'q': "sadsadn: which city is the Eiffel tower in"}
    assert api(args) == "Paris"

def test_prime():
    args = {'q': "asdsakd: which of the following numbers are primes: 7, 10, 12"}
    assert api(args) == 7

def test_james_bond():
    args = {'q': "asdsakd: who played James Bond in the film Dr No"}
    assert api(args) == "Sean Connery"
