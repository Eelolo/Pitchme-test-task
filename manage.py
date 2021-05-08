from app import create_app
from app.models import *
from app import db


if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    db.create_all()
    app.run()
