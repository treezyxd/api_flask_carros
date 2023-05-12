from flask import Flask, jsonify, request
from bd import Cars

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros', methods=['GET'])
def get_cars():
    return jsonify(
            message='Lista de carros',
            data=Cars
        )

@app.route('/carros/<int:id>', methods=['GET'])
def get_cars_by_id(id):
    for car in Cars:
        if(car.get('id') == id):
            return jsonify(car)

@app.route('/carros', methods=['POST'])
def create_car():
    car = request.json
    Cars.append(car)
    return jsonify(
            message='Carro cadastrado com sucesso',
            carro=car
        )

app.run()