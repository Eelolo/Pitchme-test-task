from app import db
from .model import Admins


def create_admin(user_id):
    admin = Admins(user_id)

    db.session.add(admin)
    db.session.commit()


def get_admin(admin_id):
    admin = Admins.query.filter_by(id=admin_id).first()

    return admin


def get_admins_data():
    data = Admins.query.all()

    admins = []
    for admin in data:
        admins.append((admin.id, admin.user_id))

    return admins


def update_admin(admin_id, **kwargs):
    admin = get_admin(admin_id)

    for key, value in kwargs.items():
        setattr(admin, key, value)

    db.session.commit()


def delete_admin(admin_id):
    admin = get_admin(admin_id)

    db.session.delete(admin)
    db.session.commit()
