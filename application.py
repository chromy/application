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
    if "largest" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        numbers = q.split(':')[2]
        numbers = map(int, numbers.split(', '))
        return largest(numbers)
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
    return 0

def largest(numbers):
    return max(numbers)

def plus(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

if __name__ == '__main__':
    app.run(debug=True)
