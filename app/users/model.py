from app import db
from flask_login import UserMixin
from app.events.model import Events

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), nullable=True)

    saved_filters = db.relationship('SavedFilters', backref='user')
    admins = db.relationship('Admins', backref='user')
    comments = db.relationship('Comments', backref='user')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.email}>"


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(Users.id))
    event_id = db.Column(db.Integer, db.ForeignKey(Events.id))
    comment = db.Column(db.String(500))

    def __init__(self, user_id, event_id, comment):
        self.user_id = user_id
        self.event_id = event_id
        self.comment = comment

    def __repr__(self):
        return f"<Comment {self.id}>"
