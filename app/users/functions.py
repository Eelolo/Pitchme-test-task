from app import db
from .model import Users, Comments


def get_users_data():
    data = Users.query.all()

    users = []
    for user in data:
        users.append((user.id, user.name, user.email))

    return users

def get_users_ids():
    data = Users.query.all()

    ids = []
    for user in data:
        ids.append(user.id)

    return ids

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


def create_comment(user_id, event_id, comment):
    comment = Comments(user_id, event_id, comment)

    db.session.add(comment)
    db.session.commit()


def get_event_comments(event_id):
    data = Comments.query.filter_by(event_id=event_id).all()

    comments = []
    for comment in data:
        comments.append((comment.user.name, event_id, comment))

    return comments