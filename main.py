from flask import Flask, jsonify, render_template, request
from data import config 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)	

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    request_value = request.get_json("name")
    print(request_value)
    print("Test")
    return jsonify({"request_value": request_value}), 200
    

@app.route('/variable')
def variable():
    return render_template('test_var.html', variable="34")

@app.route('/variable/<var>') # La url deberia ser: '/variable/34'
def variable2(var):
    return render_template('test_var2.html', variable=var)

if __name__ == '__main__':
    app.run(debug=True)