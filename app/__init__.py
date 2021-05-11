from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    from .views import main_bp
    app.register_blueprint(main_bp)

    from .views import admin_bp
    app.register_blueprint(admin_bp)

    from .users.views import admin_bp
    app.register_blueprint(admin_bp)

    from .cities.views import admin_bp
    app.register_blueprint(admin_bp)

    from .topics.views import admin_bp
    app.register_blueprint(admin_bp)

    from .events.views import admin_bp
    app.register_blueprint(admin_bp)

    from .saved_filters.views import admin_bp
    app.register_blueprint(admin_bp)

    from .views import auth_bp
    app.register_blueprint(auth_bp)

    from .admins.views import admin_bp
    app.register_blueprint(admin_bp)

    db.init_app(app)

    from .users.model import Users

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    return app
