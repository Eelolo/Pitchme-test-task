from app import db
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), nullable=True)

    saved_filters = db.relationship('SavedFilters', backref='user')
    admins = db.relationship('Admins', backref='user')
    messages = db.relationship('Messages', backref='user')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.email}>"


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.String(500))

    def __init__(self, user_id, message):
        self.user_id = user_id
        self.message = message

    def __repr__(self):
        return f"<Message {self.id}>"

