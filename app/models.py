from app import db
from datetime import datetime

class Todo(db.Model):
    __tablename__ = 'Todo'
    time = db.Column(db.DateTime, primary_key=True)
    content = db.Column(db.String)
    status = db.Column(db.Integer)

    def __init__(self, content):
        self.time = datetime.now()
        self.content = content
        self.status = 0
    def __repr__(self):
        return '<Todo: {} at {}, {}.>'.format(self.content, self.time, self.status)