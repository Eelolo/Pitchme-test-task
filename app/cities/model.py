from app import db


class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name


def create_city(name):
    city = Cities(name)

    db.session.add(city)
    db.session.commit()


def get_city(city_id):
    city = Cities.query.filter_by(id=city_id).first()

    return city


def get_cities_data():
    data = Cities.query.all()

    cities = []
    for city in data:
        cities.append((city.id, city.name))

    return cities


def update_city(city_id, **kwargs):
    city = get_city(city_id)

    for key, value in kwargs.items():
        setattr(city, key, value)

    db.session.commit()


def delete_city(city_id):
    city = get_city(city_id)

    db.session.delete(city)
    db.session.commit()
