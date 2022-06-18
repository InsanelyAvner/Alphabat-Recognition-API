from flask import Flask, jsonify, request, render_template
from classifier import get_pred

# Create new flask object
app = Flask(__name__)

# Define a small route
# Function/task related to this route

@app.route("/")
def home():
    return render_template("template.html")

@app.route("/pred-alphabat", methods=["POST"])
def pred_digit():
    image = request.files.get("digit")
    prediction = get_pred(image)

    return jsonify({
        "prediction": prediction,
    }), 200


if __name__ == "__main__":
    app.run()