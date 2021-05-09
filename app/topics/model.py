from app import db


class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name


def create_topic(name):
    topic = Topics(name)

    db.session.add(topic)
    db.session.commit()
