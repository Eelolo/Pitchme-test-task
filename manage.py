from app import create_app
from app import db
from app.users.model import Users
from app.cities.model import Cities
from app.topics.model import Topics
from app.events.model import Events
from app.saved_filters.model import SavedFilters
from app.admins.model import Admins
from app.users.model import Comments


if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    db.create_all()
    app.run(debug=True)
