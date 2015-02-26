from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<int:n>')
def index(n):
    response = fizzbuzz(n)
    return render_template('index.html', response=response)

def fizzbuzz(n):
    if n % 3 == 0:
        return 'Fizz'
    return ''

if __name__ == '__main__':
    app.run(debug=True)
