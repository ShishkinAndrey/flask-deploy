import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.getenv('FLASK_APP_SETTINGS'))
db = SQLAlchemy(app)

from models import Chronicles, SuperHeroes


@app.route("/")
def show_content():
    heroes = db.session.query(SuperHeroes).all()
    chronicles = db.session.query(Chronicles).all()
    return render_template('witcher.html', heroes=heroes, chronicles=chronicles)


if __name__ == "__main__":
    app.run()
