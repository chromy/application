import math
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/api')
def index():
    q = request.args.get('q')
    print 'q', q
    print 'args', request.args
    try:
        return str(api(request.args))
    except Exception, e:
        return str(0)

@app.route('/api2')
def index2():
    q = request.args.get('q')
    print 'q', q
    print 'args', request.args
    return str(api(request.args))

def api(args):
    q = args['q']
    if "largest" in q or "primes" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        numbers = q.split(':')[2]
        numbers = map(int, numbers.split(', '))
        if "largest" in q:
            return largest(numbers)
        else:
            return prime(numbers)
    elif "plus" in q or "multiplied" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        text = text.split(' ')
        x = int(text[3])
        y = int(text[5])
        if "plus" in q:
            return plus([x, y])
        else:
            return x * y
    elif "square and a cube" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        number_str = q.split(':')[2]
        numbers = map(int, number_str.split(','))
        return square_and_cube(numbers)
    elif "Eiffel tower in" in q:
        return "Paris"
    return -1

def largest(numbers):
    return max(numbers)

def plus(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def square_and_cube(numbers):
    for n in numbers:
        if is_square_and_cube(n):
            return n

def is_square_and_cube(number):
    square_root = number ** 0.5
    cube_root = number ** (1/3.0)
    return equal_float(square_root, int(square_root)) and equal_float(cube_root, int(cube_root))

def equal_float(a, b):
    return abs(a - b) < 0.00001

def prime(numbers):
    for n in numbers:
        if is_prime(n):
            return n
    return -100

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

if __name__ == '__main__':
    app.run(debug=True)
