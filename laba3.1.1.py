from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/number', methods = ['GET'])
def task1():
    data = int(request.args["param"])
    result = {
        'number': round(data * random.random() * 10, 3)
    }
    return result

@app.route('/number', methods = ['POST'])
def task2():
    data = int(request.json['jsonParam'])
    operations = ['sum', 'sub', 'mul', 'div']
    result = {
        'number': round(data * random.random() * 10, 3),
        'operation': operations[random.randint(0, 3)]
    }
    return result

@app.route('/number', methods = ['DELETE'])
def task3():
    data = int(request.json['jsonParam'])
    operations = ['sum', 'sub', 'mul', 'div']
    result = {
        'number': round(data * random.random() * 10, 3),
        'operation': operations[random.randint(0, 3)]
    }
    return result