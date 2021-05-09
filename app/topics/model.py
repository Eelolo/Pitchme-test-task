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


def get_topic(topic_id):
    topic = Topics.query.filter_by(id=topic_id).first()

    return topic


def get_topics_data():
    data = Topics.query.all()

    topics = []
    for topic in data:
        topics.append((topic.id, topic.name))

    return topics


def update_topic(topic_id, **kwargs):
    topic = get_topic(topic_id)

    for key, value in kwargs.items():
        setattr(topic, key, value)

    db.session.commit()
