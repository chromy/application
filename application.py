import math
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/api')
def index():
    q = request.args.get('q')
    try:
        result = str(api(request.args))
        print q, '=>', result
        return result
    except Exception, e:
        return str(0)

@app.route('/api2')
def index2():
    q = request.args.get('q')
    result = str(api(request.args))
    print q, '=>', result
    return result

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
    elif "plus" in q or "multiplied" in q or "minus" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        text = text.split(' ')
        x = int(text[3])
        y = int(text[5])
        if "plus" in q:
            return plus([x, y])
        elif "multiplied" in q:
            return x * y
        else:
            return x - y
    elif "Fibonacci" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        index = text.split(' ')[4][:-2]
        return fibo(int(index))
    elif "square and a cube" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        number_str = q.split(':')[2]
        numbers = map(int, number_str.split(','))
        return square_and_cube(numbers)
    elif "Eiffel tower in" in q:
        return "Paris"
    elif "James Bond" in q:
        return "Sean Connery"
    elif "currency" in q and "Spain":
        return "peseta"
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

def fibo(n):
    if n < 2:
        return n
    return fibo(n-2) + fibo(n-1)

if __name__ == '__main__':
    app.run(debug=True)
