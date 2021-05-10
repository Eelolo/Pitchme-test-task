from app import db


class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    saved_filters = db.relationship('SavedFilters', backref='topic')
    events = db.relationship('Events', backref='topic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Topic {self.name}>"
