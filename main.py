from flask import Flask, jsonify

api = Flask(__name__)

if __name__ == "__main__":
    api.run(debug=True)

@api.route('/api')
def ola_mundo():
    return jsonify({'msg': 'Olá Mundo!'})
