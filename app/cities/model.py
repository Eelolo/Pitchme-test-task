from app import db


class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    events = db.relationship('Events', backref='city')
    saved_filters = db.relationship('SavedFilters', backref='city')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<City {self.name}>"
