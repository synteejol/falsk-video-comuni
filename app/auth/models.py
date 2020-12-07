from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app import db




class AuthUser(UserMixin, db.Model):
    __tablename__ = "authusers"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    #email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    ruolo = db.Column(db.String(20), nullable=False)


    def __repr__(self):
        return '<AuthUser {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return self.ruolo == 'admin'
