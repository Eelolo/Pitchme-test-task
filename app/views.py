from flask import Blueprint, render_template
from .cities.functions import get_cities_data, get_cities_names, get_city_name
from .events.functions import get_events_data
from .saved_filters.functions import get_saved_filters_data
from .topics.functions import get_topics_data, get_topics_names, get_topic_name
from .users.functions import get_users_data

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    cities_names = get_cities_names()
    topics_names = get_topics_names()
    events = get_events_data()

    for event in events:
        event[5] = get_topic_name(event[5])
        event[6] = get_city_name(event[6])

    return render_template(
        'index.html', cities_names=cities_names,
        topics_names=topics_names, events=events
    )


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/')
def admin():
    users = get_users_data()
    cities = get_cities_data()
    topics = get_topics_data()
    events = get_events_data()
    saved_filters = get_saved_filters_data()

    return render_template(
        'admin_page.html',
        users=users, cities=cities, topics=topics,
        events=events, saved_filters=saved_filters
    )
