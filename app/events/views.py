from flask import request, render_template, redirect
from .functions import create_event, get_event, update_event, delete_event
from app.cities.functions import get_cities_ids
from app.topics.functions import get_topics_ids
from app.views import admin_bp
from datetime import datetime


@admin_bp.route('/create_event/', methods=['GET', 'POST'])
def admin_create_event():
    cities_ids = get_cities_ids()
    topics_ids = get_topics_ids()

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Create':
            name = request.form.get('name')
            description = request.form.get('description')
            start_at = datetime.strptime(request.form.get('start_at'), "%Y-%m-%d %H:%M")
            end_at = datetime.strptime(request.form.get('end_at'), "%Y-%m-%d %H:%M")
            topic_id = request.form.get('topic_select')
            city_id = request.form.get('city_select')

            if name and description and start_at and end_at and city_id and topic_id:
                create_event(name, description, start_at, end_at, topic_id, city_id)
            else:
                return render_template('event_form.html', cities_ids=cities_ids)

        return redirect('/admin')

    return render_template('event_form.html', topics_ids=topics_ids, cities_ids=cities_ids)


@admin_bp.route('/update_event/<event_id>/', methods=['GET', 'POST'])
def admin_update_event(event_id):
    event = get_event(event_id)
    start_at = event.start_at.strftime("%Y-%m-%d %H:%M")
    end_at = event.end_at.strftime("%Y-%m-%d %H:%M")
    data = event.id, event.name, event.description, start_at, end_at, event.topic_id , event.city_id
    topics_ids = get_topics_ids()
    cities_ids = get_cities_ids()

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Update':
            name = request.form.get('name')
            description = request.form.get('description')
            start_at = datetime.strptime(request.form.get('start_at'), "%Y-%m-%d %H:%M")
            end_at = datetime.strptime(request.form.get('end_at'), "%Y-%m-%d  %H:%M")
            topic_id = request.form.get('topic_select')
            city_id = request.form.get('city_select')

            if name and description and start_at and end_at and topic_id and city_id:
                    update_event(
                        event_id, name=name, description=description, start_at=start_at,
                        end_at=end_at, topic_id=topic_id, city_id=city_id
                    )
            else:
                return render_template('event_form.html', data=data, cities_ids=cities_ids)

        return redirect('/admin')

    return render_template('event_form.html', data=data, topics_ids=topics_ids, cities_ids=cities_ids)


@admin_bp.route('/delete_event/<event_id>/')
def admin_delete_event(event_id):
    delete_event(event_id)

    return redirect('/admin')
