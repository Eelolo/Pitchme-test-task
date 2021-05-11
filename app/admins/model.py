from app import db


class Admins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f"<Admin {self.user_id}>"
