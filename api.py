from flask import Flask, request, jsonify
from mojang import Client

app = Flask(__name__)

@app.route('/verify/', methods=['POST'])
def verify_token():
    body = request.json
    token = body.get('token')
    uuid = body.get('uuid')
    if not token:
        return jsonify({"error": "Token is required"}), 400

    if not uuid:
        return jsonify({"error": "uuid is required"}), 400

    try:
        client = Client(bearer_token=token)
        profile = client.get_profile()
    except:
        return jsonify({"result": False}), 400

    if profile.id== uuid:
        return jsonify({"result": True}), 200
    else:
        return jsonify({"result": False}), 400


if __name__ == '__main__':
    app.run(debug=False,port=5025)
