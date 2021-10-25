from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__, static_folder="/root/delcibo/app/static", template_folder='/root/delcibo/app/templates')

app.config.from_object('config')
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

from app import views, models, views_admin, HallControl, RestControl, MenuControl, UserControl, OrderControl, render



