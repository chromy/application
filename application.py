from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/api')
def index():
    q = request.args.get('q')
    print 'q', q
    print 'args', request.args
    return render_template('index.html', response=1)

if __name__ == '__main__':
    app.run(debug=True)
