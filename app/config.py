from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
import pymysql

# from flask_migrate import Migrate
pymysql.install_as_MySQLdb()
# from flask_bootstrap import Bootstrap
# '+os.getenv('MYSQL_PORT')+'


# login = LoginManager()


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:rootpass@'+os.getenv('MYSQL_HOST')+':3306/'+os.getenv('MYSQL_DATABASE')
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:rootpass@dbapp:3306/comunidb'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


# class App():
#   app = Flask(__name__)
#   login = LoginManager()
#   db = SQLAlchemy(app)

#   def configApp(self):
#     self.app.config.from_object(Config)
  
#   def manageDb(self):
#     self.db.init_app(self.app)
#     self.db.create_all()
  
#   def manageLogin(self):
#     self.login.session_protection = "strong"
    
#     self.login.login_view = 'auth_blueprint.login'#'login'


    

# def create_app():
#   app = Flask(__name__)
#   app.config.from_object(Config)
#   # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootpass@db_app:3306/comunidb'
  
  
#   return app

# def create_db(app):
#   db = SQLAlchemy(app)
#   db.init_app(app)
#   db.create_all()

# #   return db



# def importaIlNecessario():
#   from auth.views import login
#   from auth.models import AuthUser

    




