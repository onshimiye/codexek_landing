from flask import Flask, redirect, request, url_for

app = Flask(__name__)


@app.route("/code")
def code():
    code = request.args.get("code")

    return code


if __name__== "__main__":
    app.run(debug=True)
