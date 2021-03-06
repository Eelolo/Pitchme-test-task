from flask import request, render_template, redirect, flash
from .functions import create_city, get_city, update_city, delete_city
from app.views import admin_bp, admin_login_required


@admin_bp.route('/create_city/', methods=['GET', 'POST'])
@admin_login_required
def admin_create_city():
    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Create':
            name = request.form.get('name')

            if name:
                create_city(name)

            flash(f'City {name} created')

        return redirect('/admin')

    return render_template('city_form.html')


@admin_bp.route('/update_city/<city_id>/', methods=['GET', 'POST'])
@admin_login_required
def admin_update_city(city_id):
    city = get_city(city_id)
    data = city.id, city.name

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Update':
            name = request.form.get('name')

            if name:
                update_city(city_id, name=name)

            flash(f'City {data[1]} updated')

        return redirect('/admin')

    return render_template('city_form.html', data=data)


@admin_bp.route('/delete_city/<city_id>/')
@admin_login_required
def admin_delete_city(city_id):
    city = get_city(city_id)
    delete_city(city_id)

    flash(f'City {city.name} deleted')
    return redirect('/admin')
