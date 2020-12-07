from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import pymysql


app = Flask(__name__)
app.config.from_object(Config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootpass@dbapp:3306/comunidb'

db = SQLAlchemy(app)
db.init_app(app)

login = LoginManager()
login.session_protection = "strong"
login.login_view = 'auth_blueprint.login'
login.init_app(app)

from auth.models import AuthUser
from auth.views import auth_blueprint
app.register_blueprint(auth_blueprint)