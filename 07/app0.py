from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/intro")
def intro():
    return jsonify({
        "name": "John",
        "age": 20,
        "married": True,
        "car": None,
    }), 404


if __name__ == "__main__":
    app.run(debug=True)


# json vs python dict
# '' -> ""
# None -> null
# True/False -> true/false
