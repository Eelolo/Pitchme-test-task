from app import db


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


def create_saved_filter(user_id, start_from, start_to, city_id, topic_id):
    saved_filter = SavedFilters(user_id, start_from, start_to, city_id, topic_id)

    db.session.add(saved_filter)
    db.session.commit()
