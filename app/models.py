from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), nullable=True)


class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text(1000))
    start_at = db.Column(db.DateTime())
    end_at = db.Column(db.DateTime())
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))


class EventTopics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    # только уникальные записи, обеспечить позже


class SavedFilters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    start_from = db.Column(db.DateTime())
    start_to = db.Column(db.DateTime())
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
