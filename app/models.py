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


class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name


class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name


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

class EventTopics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    # только уникальные записи, обеспечить позже

    def __init__(self, topic_id, event_id):
        self.topic_id = topic_id
        self.event_id = event_id

class SavedFilters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    start_from = db.Column(db.DateTime())
    start_to = db.Column(db.DateTime())
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))

    def __init__(self, user_id, start_from, start_to, city_id, topic_id):
        self.user_id = user_id
        self.start_from = start_from
        self.start_to = start_to
        self.city_id = city_id
        self.topic_id = topic_id