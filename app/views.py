from flask import Blueprint, render_template, request, redirect, url_for, flash
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, logout_user, login_user, login_required
from .cities.functions import get_cities_data, get_cities_names
from .cities.model import Cities
from .events.functions import get_events_data, get_event
from .events.model import Events
from .saved_filters.functions import (
    get_saved_filters_data, delete_saved_filter, get_saved_filter, create_saved_filter
)
from .topics.functions import get_topics_data, get_topics_names
from .topics.model import Topics
from .users.functions import get_users_data, create_comment, get_event_comments
from .users.model import Users
from .admins.functions import get_admins_data
from .admins.model import Admins
from app import db
from datetime import datetime


main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    cities_names = get_cities_names()
    topics_names = get_topics_names()

    filters = ''
    city_name = ''
    topic_name = ''
    start_at = ''
    end_at = ''
    username = ''
    if not current_user.is_anonymous:
        username = current_user.name

        user = Users.query.filter_by(id=current_user.id).one()
        filters = list(user.saved_filters)



    query = Events.query

    if request.method == 'POST':
        if request.form.get('f_set'):
            f_set_id = int(request.form.get('f_set').split(' ')[-1])
            s_f = get_saved_filter(f_set_id)
            city_name = Cities.query.filter_by(id=s_f.city_id).one().name
            topic_name = Topics.query.filter_by(id=s_f.topic_id).one().name
            start_at = datetime.strftime(s_f.start_from, "%Y-%m-%d %H:%M")
            end_at = datetime.strftime(s_f.start_to, "%Y-%m-%d %H:%M")
        else:
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
        'index.html', cities_names=cities_names, topics_names=topics_names, events=events, filters=filters,
        city_name=city_name, topic_name=topic_name, start_at=start_at, end_at=end_at, username=username
    )


@main_bp.route('/create_f_set/', methods=['POST'])
@login_required
def create_f_set():
    city_name = request.form.get('city_select')
    topic_name = request.form.get('topic_select')

    if city_name and city_name != "Choose city name":
        city_id = Cities.query.filter_by(name=city_name).one().id
    else:
        city_id = None

    if topic_name and topic_name != "Choose topic name":
        topic_id = Topics.query.filter_by(name=topic_name).one().id
    else:
        topic_id = None

    start_at = request.form.get('start_at')
    end_at = request.form.get('end_at')
    try:
        start_at = datetime.strptime(start_at, "%Y-%m-%d %H:%M")
        end_at = datetime.strptime(end_at, "%Y-%m-%d %H:%M")
    except ValueError:
        start_at = None
        end_at = None

    if current_user.id and city_id and topic_id and start_at and end_at:
        create_saved_filter(current_user.id, start_at, end_at, city_id, topic_id)

    return redirect(url_for('main.index'))


@main_bp.route('/delete_f_set/<f_set_id>/')
@login_required
def delete_f_set(f_set_id):
    delete_saved_filter(f_set_id)

    return redirect(url_for('main.index'))

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


def admin_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:

            return redirect(url_for('admin.admin_login', next=request.url))

        return f(*args, **kwargs)

    return decorated_function


@admin_bp.route('/')
@admin_login_required
def admin():
    users = get_users_data()
    admins = get_admins_data()
    cities = get_cities_data()
    topics = get_topics_data()
    events = get_events_data()
    saved_filters = get_saved_filters_data()

    return render_template(
        'admin_page.html',
        users=users, admins=admins, cities=cities, topics=topics,
        events=events, saved_filters=saved_filters
    )


@admin_bp.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = Users.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again')
            return redirect(url_for('admin.admin_login'))

        if Admins.query.filter_by(user_id=user.id).all():
            login_user(user, remember=remember)
            return redirect(url_for('admin.admin'))
        else:
            flash('You are not admin user')
            return redirect(url_for('admin.admin_login'))

    return render_template('login.html')


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if request.form.get('cancel-btn'):
            return redirect(url_for('main.index'))

        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        user = Users.query.filter_by(email=email).first()

        if user and user.email != '':
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('auth.signup'))

        if user and user.email != '':
            new_user = Users(email=email, name=name, password=generate_password_hash(password, method='sha256'))

            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('auth.login'))

    return render_template('signup.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('cancel-btn'):
            return redirect(url_for('main.index'))

        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = Users.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again')
            return redirect(url_for('auth.login'))

        login_user(user, remember=remember)
        return redirect(url_for('main.index'))

    return render_template('login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main_bp.route('/event_page/<event_id>', methods=['GET', 'POST'])
def event_page(event_id):
    event = get_event(event_id)
    name = event.name
    description = event.description
    start_at = datetime.strftime(event.start_at, "%Y-%m-%d %H:%M")
    end_at = datetime.strftime(event.end_at, "%Y-%m-%d %H:%M")
    topic_name = Topics.query.filter_by(id=event.topic_id).one().name
    city_name = Cities.query.filter_by(id=event.city_id).one().name

    if current_user.is_authenticated:
        user_name = current_user.name
        comments = get_event_comments(event_id)
    else:
        user_name = ''
        comments = ''

    if request.method == 'POST':
        comment = request.form.get('comment_area')

        if comment:
            create_comment(current_user.id, event_id, comment)

    return render_template(
        'event_page.html', name=name, description=description, start_at=start_at,
        end_at=end_at, topic_name=topic_name, city_name=city_name, user_name=user_name,
        comments=comments, event_id=event_id
    )
