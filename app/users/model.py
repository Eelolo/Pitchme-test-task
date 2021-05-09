from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), nullable=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
