from flask import Flask, render_template, request, redirect, url_for
# from conf import create_db, create_app, importaIlNecessario
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import current_user, UserMixin,  LoginManager, login_user, logout_user, login_required, fresh_login_required, confirm_login
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootpass@dbapp:3306/comunidb'

#MySQLdb.connect(user='root', passwd='rootpass', host="dbapp", port=3306, dbname="comunidb")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


login = LoginManager()
login.session_protection = "strong"
login.login_view = 'auth_blueprint.login'
login.init_app(app)

db = SQLAlchemy(app)
db.init_app(app)
db.create_all()

from auth.models import AuthUser
from auth.views import auth_blueprint
from sez1.views import sez1_bp
from manage_sez.views import sezioni_bp
from manage_video.views import video_bp
app.register_blueprint(auth_blueprint)
app.register_blueprint(sez1_bp)
app.register_blueprint(sezioni_bp)
app.register_blueprint(video_bp)


@app.route("/first")
@fresh_login_required
def view_first_page():
    return render_template("index.html", title="First page")

@app.route("/second")
@fresh_login_required
def view_second_page():
    return render_template("index.html", title="Second page")

@login.user_loader
def load_authuser(id):
    return AuthUser.query.get(int(id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('sez1_bp.view_home'))

if __name__ == '__main__':
    
    app.run(host='0.0.0.0')
