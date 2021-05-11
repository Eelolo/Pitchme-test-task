from flask import request, render_template, redirect
from .functions import create_topic, get_topic, update_topic, delete_topic
from app.views import admin_bp, admin_login_required


@admin_bp.route('/create_topic/', methods=['GET', 'POST'])
@admin_login_required
def admin_create_topic():
    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Create':
            name = request.form.get('name')

            if name:
                create_topic(name)

        return redirect('/admin')

    return render_template('topic_form.html')


@admin_bp.route('/update_topic/<topic_id>/', methods=['GET', 'POST'])
@admin_login_required
def admin_update_topic(topic_id):
    topic = get_topic(topic_id)
    data = topic.id, topic.name

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Update':
            name = request.form.get('name')

            if name:
                update_topic(topic_id, name=name)

        return redirect('/admin')

    return render_template('topic_form.html', data=data)


@admin_bp.route('/delete_topic/<topic_id>/')
@admin_login_required
def admin_delete_topic(topic_id):
    delete_topic(topic_id)

    return redirect('/admin')
