
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/calculate")
def calculate():

    values = []

    try:
        for i in range(1, 4):
            raw = request.args.get(f"m{i}")

            if raw is None or raw.strip() == "":
                return jsonify({
                    "error": f"Missing subject mark m{i}"
                }), 400

            values.append(float(raw))

    except ValueError:
        return jsonify({
            "error": "Marks must be numeric"
        }), 400

    if any(mark < 0 or mark > 100 for mark in values):
        return jsonify({
            "error": "Each mark must be between 0 and 100"
        }), 400

    total = sum(values)
    average = round(total / 3, 2)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return jsonify({
        "marks": values,
        "total": total,
        "average": average,
        "grade": grade
    })


@app.post("/calculate")
def calculate_form():

    try:
        data = request.get_json(silent=True) or request.form

        marks = [
            float(data.get("m1", "")),
            float(data.get("m2", "")),
            float(data.get("m3", ""))
        ]

        if any(mark < 0 or mark > 100 for mark in marks):
            return jsonify({
                "error": "Marks must be between 0 and 100"
            }), 400

    except (ValueError, TypeError):
        return jsonify({
            "error": "Please enter valid numeric marks"
        }), 400

    total = sum(marks)
    average = round(total / 3, 2)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return jsonify({
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
