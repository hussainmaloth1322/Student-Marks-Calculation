
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate")
def calculate():
    try:
        m1 = float(request.args.get("m1"))
        m2 = float(request.args.get("m2"))
        m3 = float(request.args.get("m3"))

        marks = [m1, m2, m3]

        if any(not (0 <= mark <= 100) for mark in marks):
            return jsonify({
                "error": "Marks must be between 0 and 100"
            }), 400

        total = sum(marks)
        average = round(total / 3, 2)

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        return jsonify({
            "marks": marks,
            "total": total,
            "average": average,
            "grade": grade
        })

    except (ValueError, TypeError):
        return jsonify({
            "error": "Please enter valid marks"
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
