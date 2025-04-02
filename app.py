from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Render!'

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    response = requests.post('http://bot_endpoint/send_message', json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
