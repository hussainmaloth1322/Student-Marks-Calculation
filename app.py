"""Flask API used by the Docker image and Selenium tests."""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "Student Marks Calculation Application"

@app.get("/calculate")
def calculate():
    values = []
    try:
        for i in range(1, 4):
            raw = request.args.get(f"m{i}")
            if raw is None or raw.strip() == "":
                return jsonify({"error": f"Missing subject mark m{i}"}), 400
            values.append(float(raw))
    except ValueError:
        return jsonify({"error": "Marks must be numeric"}), 400

    if any(mark < 0 or mark > 100 for mark in values):
        return jsonify({"error": "Each mark must be between 0 and 100"}), 400

    total = sum(values)
    return jsonify({
        "marks": values,
        "total": total,
        "average": round(total / 3, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
