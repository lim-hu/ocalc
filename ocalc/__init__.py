from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{app.root_path}/ocalc.db"
db = SQLAlchemy(app)

from . import routes

