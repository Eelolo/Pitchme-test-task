from app import db


class EventTopics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    # только уникальные записи, обеспечить позже

    def __init__(self, topic_id, event_id):
        self.topic_id = topic_id
        self.event_id = event_id


def create_event_topic(topic_id, event_id):
    event_topic = EventTopics(topic_id, event_id)

    db.session.add(event_topic)
    db.session.commit()
