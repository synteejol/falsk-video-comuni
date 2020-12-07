from flask_sqlalchemy import SQLAlchemy
from app import db
#db = SQLAlchemy()

class Sezioni(db.Model):
    __tablename__ = "sezioni"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    video = db.relationship('Video', backref='sezioni', lazy=True)

class Video(db.Model):
    __tablename__ = "video"
    id = db.Column(db.Integer, primary_key=True)
    codice = db.Column(db.String(30), nullable=False)
    sez = db.Column(db.Integer, db.ForeignKey('sezioni.id'),
        nullable=False)
    desc = db.Column(db.String(200))

    def __repr__(self):
        return '<Video %r>' % self.id