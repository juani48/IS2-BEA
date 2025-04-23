from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/variable')
def variable():
    return render_template('test_var.html', variable="34")

@app.route('/variable/<var>') # La url deberia ser: '/variable/34'
def variable2(var):
    return render_template('test_var2.html', variable=var)

if __name__ == '__main__':
    app.run(debug=True)