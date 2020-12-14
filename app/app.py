from flask import Flask, render_template, request, redirect, render_template_string, session, url_for, flash, g
from datetime import datetime, timedelta 
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import current_user, UserMixin,  LoginManager, login_user, logout_user, login_required, fresh_login_required, confirm_login
import pymysql
pymysql.install_as_MySQLdb()
# import MySQLdb
import os
from os.path import join, dirname, realpath


app = Flask(__name__)

login = LoginManager()
login.session_protection = "strong"
login.login_view = 'auth_blueprint.login'
login.init_app(app)

app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootpass@'+os.getenv('MYSQL_HOST')+':3306/'+os.getenv('DB_NAME') #dbapp:3306/comunidb'

#MySQLdb.connect(user='root', passwd='rootpass', host="dbapp", port=3306, dbname="comunidb")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False







db = SQLAlchemy(app)
db.init_app(app)
db.create_all()

from models.models import Sezioni
from auth.models import AuthUser
from auth.views import auth_blueprint
from sez1.views import sez1_bp
from manage_sez.views import sezioni_bp
from manage_video.views import video_bp
app.register_blueprint(auth_blueprint)
app.register_blueprint(sez1_bp)
app.register_blueprint(sezioni_bp)
app.register_blueprint(video_bp)


@app.route("/")
# @fresh_login_required
def view_first_page():
    return render_template("snippets/animazioneLogo.html", sezioni = Sezioni.query.all())

@app.route("/home")

def view_home_page():
    return render_template("home.html", sezioni = Sezioni.query.all())


# @app.route("/second")
# @fresh_login_required
# def view_second_page():
#     return render_template("index.html", title="Second page")

@app.before_request
def before_request():
    #session.permanent = True
    session.modified = True
    app.permanent_session_lifetime = timedelta(minutes=20)
    #g.user = current_user

@login.user_loader
def load_authuser(id):
    return AuthUser.query.get(int(id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('view_home_page'))

if __name__ == '__main__':

    app.run(host='0.0.0.0')
