from flask import Flask, request, jsonify

__name__ = "main"

app = Flask(__name__)

@app.route('/')
def index():
    return 'Listener'

@app.route('/node-recv', methods=['POST'])
def noderecv():
    data = request.get_json()
    print("Received:", data)
    response = {'message': 'successful'}
    return jsonify(response)

if __name__ == "main":
    app.run(debug=True)