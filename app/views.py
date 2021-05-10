from flask import Blueprint, render_template
from .cities.functions import get_cities_data
from .event_topics.model import get_event_topics_data
from .events.model import get_events_data
from .saved_filters.model import get_saved_filters_data
from .topics.model import get_topics_data
from .users.functions import get_users_data


main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/')
def admin():
    users = get_users_data()
    cities = get_cities_data()
    topics = get_topics_data()
    events = get_events_data()
    event_topics = get_event_topics_data()
    saved_filters = get_saved_filters_data()

    return render_template(
        'admin_page.html',
        users=users, cities=cities, topics=topics, events=events,
        event_topics=event_topics, saved_filters=saved_filters
    )
