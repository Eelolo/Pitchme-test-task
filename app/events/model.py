from app import db


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text(1000))
    start_at = db.Column(db.DateTime())
    end_at = db.Column(db.DateTime())
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

    comments = db.relationship('Comments', backref='event')

    def __init__(self, name, description, start_at, end_at, topic_id, city_id):
        self.name = name
        self.description = description
        self.start_at = start_at
        self.end_at = end_at
        self.topic_id = topic_id
        self.city_id = city_id

    def __repr__(self):
        return f"<Event {self.name}>"
