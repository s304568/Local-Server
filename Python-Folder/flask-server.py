from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

names = {
    'Alex': {'first-name': 'Alex', 'surname': 'Bowker', 'age': 22},
    'Nic': {'first-name': 'Nic', 'surname': 'Grigore', 'age': 26}
}

@app.route('/names', methods = ["GET"])
def get_name():
    return jsonify(names)

if __name__ == "__main__":
    app.run()