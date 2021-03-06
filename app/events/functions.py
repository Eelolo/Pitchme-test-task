from app import db
from .model import Events


def create_event(name, description, start_at, end_at, topic_id, city_id):
    event = Events(name, description, start_at, end_at, topic_id, city_id)

    db.session.add(event)
    db.session.commit()


def get_event(event_id):
    event = Events.query.filter_by(id=event_id).first()

    return event


def get_all_events():
    events = Events.query.all()

    return events

def get_events_data(ids_or_names='ids', events=None):
    if not events and events != None:
        return []
    elif not events:
        events = get_all_events()

    data = []
    for event in events:
        if ids_or_names == 'ids':
            fields = [
                event.id, event.name, event.description, event.start_at,
                event.end_at, event.topic_id, event.city_id
            ]
        else:
            fields = [
                event.id, event.name, event.description, event.start_at,
                event.end_at, event.topic.name, event.city.name
            ]

        data.append(
            fields
        )

    return data


def update_event(event_id, **kwargs):
    event = get_event(event_id)

    for key, value in kwargs.items():
        setattr(event, key, value)

    db.session.commit()


def delete_event(event_id):
    event = get_event(event_id)

    db.session.delete(event)
    db.session.commit()
