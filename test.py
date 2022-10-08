from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    pass


# @app.route("/contact")
# def contact():
#     pass

app.run(debug=True)
