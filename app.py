from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/healthcheck')
def healthcheck():
    return jsonify({"status": "OK"}), 200

@app.route('/v2/app')
def version():
    return jsonify({"body": "This is App v2"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
