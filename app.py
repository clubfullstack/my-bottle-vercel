from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask, a new test to enable data exchange!"

@app.route('/add_card', methods=['POST'])
def add_card():
    data = request.get_json()
    return jsonify({"status": "Card added", "data": data}), 201

@app.route('/cards', methods=['GET'])
def list_cards():
    cards = [
        {"name": "John Doe", "title": "Developer", "pagina_online": "http://johndoe.com", "instagram": "johndoe", "classification": "Tech"}
    ]
    return jsonify({"cards": cards})

if __name__ == '__main__':
    app.run()
