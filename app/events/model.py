from app import db


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
