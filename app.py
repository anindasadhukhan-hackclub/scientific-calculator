from flask import Flask, request, render_template
import scientific_calculator as calc
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        operation = request.form["operation"]

        try:
            # Arithmetic & Power & Percentage
            if operation in ["add", "sub", "mul", "div", "per", "pow"]:
                x = float(request.form["x"])
                y = float(request.form["y"])

                if operation == "add":
                    result = calc.add(x, y)
                elif operation == "sub":
                    result = calc.subtract(x, y)
                elif operation == "mul":
                    result = calc.multiply(x, y)
                elif operation == "div":
                    result = calc.divide(x, y)
                elif operation == "per":
                    result = calc.percentage(x, y)
                elif operation == "pow":
                    result = calc.power(x, y)

            # Trigonometry & Square root
            elif operation in ["sin", "cos", "tan", "sqrt"]:
                x = float(request.form["x"])

                if operation == "sin":
                    result = calc.sin_val(x)
                elif operation == "cos":
                    result = calc.cos_val(x)
                elif operation == "tan":
                    result = calc.tan_val(x)
                elif operation == "sqrt":
                    result = calc.sqrt_val(x)

            # Logarithm
            elif operation == "log":
                x = float(request.form["x"])
                base = float(request.form["y"])
                result = calc.log_val(x, base)

            # Statistics
            elif operation in ["mean", "median", "mode", "max", "min"]:
                nums = request.form["numbers"]
                numbers = list(map(float, nums.split(",")))

                if operation == "mean":
                    result = calc.mean(numbers)
                elif operation == "median":
                    result = calc.median(numbers)
                elif operation == "mode":
                    result = calc.mode(numbers)
                elif operation == "max":
                    result = calc.maximum(numbers)
                elif operation == "min":
                    result = calc.minimum(numbers)

        except Exception:
            result = "Invalid input"

    return render_template("index.html", result=result)


# ✅ REQUIRED FOR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
