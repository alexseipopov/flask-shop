import time
from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config["SECRET_KEY"] = "secret ket"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)


class Item(db.Model):
    __tablename__ = 'Item'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.Text(), default="Nice Item")


@app.route("/")
def index():
    field = Item(name=f"{time.time()}", cost=1000)
    db.session.add(field)
    db.session.commit()
    return render_template("index.html", title="Главная страница")


# @app.route("/contact")
# def contact():
#     pass

if __name__ == "__main__":
    app.run(debug=True)
