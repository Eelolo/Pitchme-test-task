from app import db
from .model import Events


def create_event(name, description, start_at, end_at, city_id):
    event = Events(name, description, start_at, end_at, city_id)

    db.session.add(event)
    db.session.commit()


def get_event(event_id):
    event = Events.query.filter_by(id=event_id).first()

    return event


def get_events_data():
    data = Events.query.all()

    events = []
    for event in data:
        events.append(
            (event.id, event.name, event.description, event.start_at, event.end_at, event.city_id)
        )

    return events


def update_event(event_id, **kwargs):
    event = get_event(event_id)

    for key, value in kwargs.items():
        setattr(event, key, value)

    db.session.commit()


def delete_event(event_id):
    event = get_event(event_id)

    db.session.delete(event)
    db.session.commit()
