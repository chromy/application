import application
api = application.api

def test_max():
    args = {'q': "asdjsaklk: which of the following numbers is the largest: 10, 12, 120"}
    assert api(args) == 120

def test_plus():
    args = {'q': "asdjsaklk: what is 5 plus 4"}
    assert api(args) == 9

def test_minus():
    args = {'q': "asdjsaklk: what is 5 minus 4"}
    assert api(args) == 1

def test_multiplied():
    args = {'q': "asdjsaklk: what is 5 multiplied 4"}
    assert api(args) == 20

def test_square_and_cube():
    args = {'q': "asdjsaklk: which of the following numbers is both a square and a cube: 68, 1"}
    assert api(args) == '1'

def test_paris():
    args = {'q': "sadsadn: which city is the Eiffel tower in"}
    assert api(args) == "Paris"

def test_prime():
    args = {'q': "asdsakd: which of the following numbers are primes: 7, 10, 12, 2"}
    assert api(args) == '7,2'
    args = {'q': "asdsakd: which of the following numbers are primes: 7, 10, 12"}
    assert api(args) == '7'
    args = {'q': "asdsakd: which of the following numbers are primes: 524, 11"}
    assert api(args) == '11'

def test_james_bond():
    args = {'q': "asdsakd: who played James Bond in the film Dr No"}
    assert api(args) == "Sean Connery"

def test_spain_currency():
    args = {'q': "asdsakd: what currency did Spain use before the Euro"}
    assert api(args) == "peseta"

def test_fibonacci():
    args = {'q': "asdsakd: what is the 7th number in the Fibonacci sequence"}
    assert api(args) == 13
    args = {'q': "asdsakd: what is the 1st number in the Fibonacci sequence"}
    assert api(args) == 1
    args = {'q': "asdsakd: what is the 2nd number in the Fibonacci sequence"}
    assert api(args) == 1

def test_power():
    args = {'q': "asdsakd: what is 2 to the power of 2"}
    assert api(args) == 4
    args = {'q': "asdsakd: what is 1 to the power of 1000"}
    assert api(args) == 1

def test_math():
    args = {'q': "asdsakd: what is 10 plus 11 multiplied by 16"}
    assert api(args) == 186
    args = {'q': "asdsakd: what is 12 minus 2 multiplied by 3"}
    assert api(args) == 6
    args = {'q': "asdsakd: what is 4 plus 2 plus 3"}
    assert api(args) == 9
    args = {'q': "asdsakd: what is 4 multiplied by 2 plus 3"}
    assert api(args) == 11

def test_capital_usa():
    args = {'q': "asdsakd: what is the capital of USA?"}
    assert api(args) == "Washington, D.C."

def is_anagram_f():
    assert application('foo' 'ofo')
    assert not application('foo' 'offo')

def test_anagram():
    args = {'q': '2ab81530: which of the following is an anagram of "dictionary": butterfly, indicatory, abdication, incendiary'}
    assert api(args) == "indicatory"
    args = {'q': '2ab81530: which of the following is an anagram of "cat": fox, dog, tac, act'}
    assert api(args) == "tac,act"
