from flask import Flask, request, jsonify
from analyzer import analyze_html

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    html = data.get("html", "")
    result = analyze_html(html)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')