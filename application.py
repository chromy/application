from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/api')
def index():
    q = request.args.get('q')
    print 'q', q
    print 'args', request.args
    return str(api(request.args))

def api(args):
    hash = args['q'].split(':')[0]
    text = args['q'].split(':')[1]
    numbers = args['q'].split(':')[2]
    numbers = map(int, numbers.split(', '))
    if "largest" in text:
        return largest(numbers)
    elif "plus" in text:
        return plus(numbers)
    return ""

def largest(numbers):
    return max(numbers)

def plus(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

if __name__ == '__main__':
    app.run(debug=True)
