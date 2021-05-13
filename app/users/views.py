from flask import request, render_template, redirect, flash
from werkzeug.security import generate_password_hash
from .functions import create_user, get_user, update_user, delete_user
from app.views import admin_bp, admin_login_required
from app.validations import email_regex_validation, email_unique_validation


@admin_bp.route('/create_user/', methods=['GET', 'POST'])
@admin_login_required
def admin_create_user():
    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Create':
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm-password')

            if email_regex_validation(email):
                email = email_unique_validation(email, '')
                if not email:
                    flash('Email address already exists')
            else:
                email = False
                flash('Email regex check failed')

            if name and email and password and password == confirm_password:
                password = generate_password_hash(password)
                create_user(name, email, password)
            else:
                return render_template('user_form.html')

        return redirect('/admin')

    return render_template('user_form.html')


@admin_bp.route('/update_user/<user_id>/', methods=['GET', 'POST'])
@admin_login_required
def admin_update_user(user_id):
    user = get_user(user_id)
    data = user.id, user.name, user.email

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Update':
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm-password')

            if email_regex_validation(email):
                email = email_unique_validation(email, user.email)
                if not email:
                    flash('Email address already exists')
            else:
                email = False
                flash('Email regex check failed')

            if name and email:
                if password and password == confirm_password:
                    password = generate_password_hash(password, method='sha256')
                    update_user(user_id, name=name, email=email, password=password)
                else:
                    update_user(user_id, name=name, email=email)
            else:
                return render_template('user_form.html', data=data)

        return redirect('/admin')

    return render_template('user_form.html', data=data)


@admin_bp.route('/delete_user/<user_id>/')
@admin_login_required
def admin_delete_user(user_id):
    delete_user(user_id)

    return redirect('/admin')
