from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

names = {
    'Alex': {'first-name': 'Alex', 'surname': 'Bowker', 'age': 22},
    'Nic': {'first-name': 'Nic', 'surname': 'Grigore', 'age': 26}
}

animals = {
    "Joe": {"name": "Joe", "age": 3 , "type": "dog"},
    "Sam": {"name": "Sam", "age": 1.5 , "type": "fish"},
    "Sam": {"name": "Sam", "age": 23 , "type": "sharck"},
}

@app.route('/names', methods = ["GET"])
def get_name():
    return jsonify(names)

@app.route('/animals', methods = ["Get"])
def get_animals():
    animal = request.args.get("animal")
    if animal in animals:
        return jsonify(animals)
    else:
        return '', 400

if __name__ == "__main__":
    app.run()