from app import db
import datetime

class ToDo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(16))
    time = db.Column(db.Integer,default=datetime.datetime.now())
    status = db.Column(db.Integer,default=0)