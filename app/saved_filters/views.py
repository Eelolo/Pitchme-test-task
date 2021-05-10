from flask import request, render_template, redirect
from .functions import create_saved_filter, get_saved_filter, update_saved_filter, delete_saved_filter
from app.cities.functions import get_cities_ids
from app.users.functions import get_users_ids
from app.topics.functions import get_topics_ids
from app.views import admin_bp
from datetime import datetime


@admin_bp.route('/create_saved_filter/', methods=['GET', 'POST'])
def admin_create_saved_filter():
    topics_ids = get_topics_ids()
    cities_ids = get_cities_ids()
    users_ids = get_users_ids()

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Create':
            user_id = request.form.get('user_select')
            start_from = datetime.strptime(request.form.get('start_from'), "%Y-%m-%d %H:%M")
            start_to = datetime.strptime(request.form.get('start_to'), "%Y-%m-%d %H:%M")
            city_id = request.form.get('city_select')
            topic_id = request.form.get('topic_select')

            if start_from and start_to:
                create_saved_filter(user_id, start_from, start_to, city_id, topic_id)
            else:
                return render_template(
                    'saved_filter_form.html', topics_ids=topics_ids,
                    cities_ids=cities_ids, users_ids=users_ids
                )

        return redirect('/admin')

    return render_template(
        'saved_filter_form.html', topics_ids=topics_ids,
        cities_ids=cities_ids, users_ids=users_ids
    )


@admin_bp.route('/update_saved_filter/<saved_filter_id>/', methods=['GET', 'POST'])
def admin_update_saved_filter(saved_filter_id):
    topics_ids = get_topics_ids()
    cities_ids = get_cities_ids()
    users_ids = get_users_ids()

    saved_filter = get_saved_filter(saved_filter_id)
    start_from = saved_filter.start_from.strftime("%Y-%m-%d %H:%M")
    start_to = saved_filter.start_to.strftime("%Y-%m-%d %H:%M")
    data = (
        saved_filter.id,  saved_filter.user_id,  start_from,
        start_to, saved_filter.city_id,  saved_filter.topic_id
    )

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Update':
            user_id = request.form.get('user_select')
            start_from = datetime.strptime(request.form.get('start_from'), "%Y-%m-%d %H:%M")
            start_to = datetime.strptime(request.form.get('start_to'), "%Y-%m-%d %H:%M")
            city_id = request.form.get('city_select')
            topic_id = request.form.get('topic_select')

            if user_id and start_from and start_to:
                    update_saved_filter(
                        saved_filter_id, user_id=user_id, start_from=start_from,
                        start_to=start_to, city_id=city_id, topic_id=topic_id
                    )
            else:
                return render_template(
                    'saved_filter_form.html', data=data, topics_ids=topics_ids,
                    cities_ids=cities_ids, users_ids=users_ids
                )

        return redirect('/admin')

    return render_template(
        'saved_filter_form.html', data=data, topics_ids=topics_ids,
        cities_ids=cities_ids, users_ids=users_ids
    )


@admin_bp.route('/delete_saved_filter/<saved_filter_id>/')
def admin_delete_saved_filter(saved_filter_id):
    delete_saved_filter(saved_filter_id)

    return redirect('/admin')
