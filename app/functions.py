from app.cities.model import Cities
from app.topics.model import Topics
from app.events.model import Events
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound


def prepare_to_create_f_set(city_name, topic_name, start_at, end_at):
    if city_name and city_name != "Choose city name":
        city_id = Cities.query.filter_by(name=city_name).one().id
    else:
        city_id = None

    if topic_name and topic_name != "Choose topic name":
        topic_id = Topics.query.filter_by(name=topic_name).one().id
    else:
        topic_id = None

    try:
        start_at = datetime.strptime(start_at, "%Y-%m-%d %H:%M")
    except ValueError:
        start_at = None

    try:
        end_at = datetime.strptime(end_at, "%Y-%m-%d %H:%M")
    except ValueError:
        end_at = None

    return city_id, topic_id, start_at, end_at


def prepare_f_set_for_view(s_f):
    city_name, topic_name, start_at, end_at = '', '', '', ''

    try:
        city_name = Cities.query.filter_by(id=s_f.city_id).one().name
    except NoResultFound:
        pass

    try:
        topic_name = Topics.query.filter_by(id=s_f.topic_id).one().name
    except NoResultFound:
        pass

    if s_f.start_from:
        start_at = datetime.strftime(s_f.start_from, "%Y-%m-%d %H:%M")
    if s_f.start_to:
        end_at = datetime.strftime(s_f.start_to, "%Y-%m-%d %H:%M")

    return city_name, topic_name, start_at, end_at


def filtered_event_query(query, city_name, topic_name, start_at, end_at):
    if city_name:
        query = query.filter_by(city_id=Cities.query.filter_by(name=city_name).one().id)

    if topic_name:
        query = query.filter_by(topic_id=Topics.query.filter_by(name=topic_name).one().id)

    if start_at and end_at:
        query = query.filter(Events.start_at >= start_at).filter(Events.end_at <= end_at)
    elif end_at:
        query = query.filter(Events.end_at <= end_at)
    elif start_at:
        query = query.filter(Events.start_at >= start_at)

    return query
