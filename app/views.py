from flask import Blueprint, render_template


main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/')
def admin():
    return render_template('admin_page.html')
