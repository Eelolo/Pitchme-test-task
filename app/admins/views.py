from flask import request, render_template, redirect, flash
from .functions import create_admin, get_admin, update_admin, delete_admin
from app.users.functions import get_users_ids
from app.views import admin_bp, admin_login_required


@admin_bp.route('/create_admin/', methods=['GET', 'POST'])
@admin_login_required
def admin_create_admin():
    users_ids = get_users_ids()

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Create':
            user_id = request.form.get('user_select')

            create_admin(user_id)

            flash(f'User id={user_id} now is admin')

        return redirect('/admin')

    return render_template('admin_form.html', users_ids=users_ids)


@admin_bp.route('/update_admin/<admin_id>/', methods=['GET', 'POST'])
@admin_login_required
def admin_update_admin(admin_id):
    admin = get_admin(admin_id)
    data = admin.id, admin.user_id
    users_ids = get_users_ids()

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Update':
            user_id = request.form.get('user_select')

            update_admin(admin_id, user_id=user_id)

            flash(f'For admin id={data[0]} user id changed')

        return redirect('/admin')

    return render_template('admin_form.html', data=data, users_ids=users_ids)


@admin_bp.route('/delete_admin/<admin_id>/')
@admin_login_required
def admin_delete_admin(admin_id):
    admin = get_admin(admin_id)
    delete_admin(admin_id)

    flash(f'User id={admin.user_id} now is not admin')
    return redirect('/admin')
