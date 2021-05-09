from app import db


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text(1000))
    start_at = db.Column(db.DateTime())
    end_at = db.Column(db.DateTime())
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

    def __init__(self, name, description, start_at, end_at, city_id):
        self.name = name
        self.description = description
        self.start_at = start_at
        self.end_at = end_at
        self.city_id = city_id


def create_event(name, description, start_at, end_at, city_id):
    event = Events(name, description, start_at, end_at, city_id)

    db.session.add(event)
    db.session.commit()
