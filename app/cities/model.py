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
