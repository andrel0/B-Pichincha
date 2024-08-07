from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"

@app.route('/DevOps', methods=['POST'])
def devops():
    if request.headers.get('X-Parse-REST-API-Key') != API_KEY:
        return "ERROR", 403

    data = request.get_json()
    if not data:
        return "ERROR", 400

    response = {
        "message": f"Hello {data.get('to')} your message will be send"
    }
    return jsonify(response), 200

@app.route('/DevOps', methods=['GET', 'PUT', 'DELETE'])
def devops_error():
    return "ERROR", 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
