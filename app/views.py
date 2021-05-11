from flask import Blueprint, render_template, request
from .cities.functions import get_cities_data, get_cities_names
from .cities.model import Cities
from .events.functions import get_events_data
from .events.model import Events
from .saved_filters.functions import get_saved_filters_data
from .topics.functions import get_topics_data, get_topics_names
from .topics.model import Topics
from .users.functions import get_users_data


main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    cities_names = get_cities_names()
    topics_names = get_topics_names()

    city_name = ''
    topic_name = ''
    start_at = ''
    end_at = ''

    query = Events.query

    if request.method == 'POST':
        city_name = request.form.get('city_select')
        topic_name = request.form.get('topic_select')
        start_at = request.form.get('start_at')
        end_at = request.form.get('end_at')

        if city_name == "Choose city name":
            city_name = ''

        if topic_name == "Choose topic name":
            topic_name = ''

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

    events = get_events_data(ids_or_names='names', events=query.all())

    return render_template(
        'index.html', cities_names=cities_names, topics_names=topics_names, events=events,
        city_name=city_name, topic_name=topic_name, start_at=start_at, end_at=end_at
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
