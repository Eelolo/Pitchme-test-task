from app import db


class EventTopics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    # только уникальные записи, обеспечить позже

    def __init__(self, topic_id, event_id):
        self.topic_id = topic_id
        self.event_id = event_id

    def __repr__(self):
        return f"<Event Topic {self.id}>"


def create_event_topic(topic_id, event_id):
    event_topic = EventTopics(topic_id, event_id)

    db.session.add(event_topic)
    db.session.commit()


def get_event_topic(event_topic_id):
    event_topic = EventTopics.query.filter_by(id=event_topic_id).first()

    return event_topic


def get_event_topics_data():
    data = EventTopics.query.all()

    event_topics = []
    for event_topic in data:
        event_topics.append(
            (event_topic.id, event_topic.topic_id, event_topic.event_id)
        )

    return event_topics


def update_event_topic(event_topic_id, **kwargs):
    event_topic = get_event_topic(event_topic_id)

    for key, value in kwargs.items():
        setattr(event_topic, key, value)

    db.session.commit()


def delete_event_topic(event_topic_id):
    event_topic = get_event_topic(event_topic_id)

    db.session.delete(event_topic)
    db.session.commit()
