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


def get_users_data():
    data = Users.query.all()

    users = []
    for user in data:
        users.append((user.name, user.email))

    return users


def get_user(user_id):
    user = Users.query.filter_by(id=user_id).first()

    return user
