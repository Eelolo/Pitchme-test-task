from app import db
from .model import Topics


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


def get_topics_ids():
    data = Topics.query.all()

    ids = []
    for topic in data:
        ids.append(topic.id)

    return ids


def update_topic(topic_id, **kwargs):
    topic = get_topic(topic_id)

    for key, value in kwargs.items():
        setattr(topic, key, value)

    db.session.commit()


def delete_topic(topic_id):
    topic = get_topic(topic_id)

    db.session.delete(topic)
    db.session.commit()
