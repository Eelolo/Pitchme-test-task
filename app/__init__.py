from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

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

    db.init_app(app)

    return app
