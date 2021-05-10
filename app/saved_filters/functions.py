from app import db
from .model import SavedFilters


def create_saved_filter(user_id, start_from, start_to, city_id, topic_id):
    saved_filter = SavedFilters(user_id, start_from, start_to, city_id, topic_id)

    db.session.add(saved_filter)
    db.session.commit()


def get_saved_filter(saved_filter_id):
    saved_filter = SavedFilters.query.filter_by(id=saved_filter_id).first()

    return saved_filter


def get_saved_filters_data():
    data = SavedFilters.query.all()

    saved_filters = []
    for saved_filter in data:
        saved_filters.append(
            (
                saved_filter.id, saved_filter.user_id, saved_filter.start_from,
                saved_filter.start_to, saved_filter.city_id, saved_filter.topic_id
            )
        )

    return saved_filters


def update_saved_filter(saved_filter_id, **kwargs):
    saved_filter = get_saved_filter(saved_filter_id)

    for key, value in kwargs.items():
        setattr(saved_filter, key, value)

    db.session.commit()


def delete_saved_filter(saved_filter_id):
    saved_filter = get_saved_filter(saved_filter_id)

    db.session.delete(saved_filter)
    db.session.commit()
