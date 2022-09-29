import json
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_alembic import Alembic

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///listing.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_type = db.Column(db.Integer, nullable=False)
    furnished = db.Column(db.Boolean, nullable=False)
    level = db.Column(db.Integer, nullable=True)
    link = db.Column(db.String, nullable=False)
    listing_no = db.Column(db.Integer, nullable=False)
    negotiable = db.Column(db.Boolean, nullable=False)
    private = db.Column(db.Boolean, nullable=False)
    collection_date = db.Column(db.String(120), nullable=False)
    publish_date = db.Column(db.String, nullable=False)
    rent = db.Column(db.Integer, nullable=False)
    rent_extra = db.Column(db.Integer, nullable=False)
    rent_full = db.Column(db.Integer, nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    surface = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    update_date = db.Column(db.DateTime, nullable=True, onupdate=datetime.now())

    def __str__(self):
        return f"{self.id}: {self.surface}, {self.rent_full}"

    def __repr__(self):
        return f"{self.id}: {self.surface}, {self.rent_full}"


db.create_all()
alembic = Alembic()
alembic.init_app(app)


def read_db():
    with open("../calculations/all-data-unfiltered.json", "r") as f:
        result = json.load(f)
        return result


@app.route("/")
def home():
    return render_template("home.html", msg="Home Site")


@app.route("/update_database/")
def update_database():
    file_data = read_db()
    for d in file_data:
        single_listing = Listing(**d)
        db.session.add(single_listing)

    db.session.commit()
    return "Success"
