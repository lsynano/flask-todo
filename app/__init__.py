from flask import Flask
import flask_sqlalchemy as sa

app = Flask(__name__)
app.config.from_object('config')

db = sa.SQLAlchemy(app)

from app import models, views
