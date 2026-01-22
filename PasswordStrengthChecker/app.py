from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/check', methods=['POST'])
def check_password():
    s = request.json.get("password", "")

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numeric = "0123456789"

    total_percentage = 0
    num_found = upper_found = lower_found = special_found = False

    for i in s:
        if i in uppercase:
            upper_found = True
        elif i in lowercase:
            lower_found = True
        elif i in numeric:
            num_found = True
        else:
            special_found = True

    if len(s) > 15:
        total_percentage += 20
    elif len(s) >= 8:
        total_percentage += 15
    elif len(s) >= 5:
        total_percentage += 10
    else:
        total_percentage += 5

    if num_found: total_percentage += 20
    if upper_found: total_percentage += 20
    if special_found: total_percentage += 20
    if lower_found: total_percentage += 20

    return jsonify({"strength": f"{total_percentage}%"})

if __name__ == "__main__":
    app.run(debug=True)
