from app import db
from .model import Users


def get_users_data():
    data = Users.query.all()

    users = []
    for user in data:
        users.append((user.id, user.name, user.email))

    return users


def get_user(user_id):
    user = Users.query.filter_by(id=user_id).first()

    return user


def create_user(name, email, password):
    user = Users(name, email, password)

    db.session.add(user)
    db.session.commit()


def update_user(user_id, **kwargs):
    user = get_user(user_id)

    for key, value in kwargs.items():
        setattr(user, key, value)

    db.session.commit()


def delete_user(user_id):
    user = get_user(user_id)

    db.session.delete(user)
    db.session.commit()
