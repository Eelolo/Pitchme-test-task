from .users.model import Users
import re
from sqlalchemy.exc import NoResultFound
from datetime import datetime


def email_regex_validation(string):
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string):
        string = False

    return string


def email_unique_validation(string):
    try:
        Users.query.filter_by(email=string).one()
        string = False
    except NoResultFound:
        pass

    return string


def datetime_validation(string):
    try:
        datetime.strptime(string, "%Y-%m-%d %H:%M")
    except ValueError:
        string = False

    return string
