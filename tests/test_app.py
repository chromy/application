import application

def test_empty():
    assert application.fizzbuzz(1) == ''
    assert application.fizzbuzz(2) == ''

def test_fizz():
    assert application.fizzbuzz(3) == 'Fizz'
    assert application.fizzbuzz(6) == 'Fizz'
