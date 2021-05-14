from app import create_app
from app import db
from app.users.model import Users, Comments
from app.users.functions import create_user
from app.validations import email_unique_validation
from app.validations import email_regex_validation
from app.cities.model import Cities
from app.cities.functions import create_city
from app.topics.model import Topics
from app.topics.functions import create_topic
from app.events.model import Events
from app.events.functions import create_event
from app.saved_filters.model import SavedFilters
from app.admins.model import Admins
from app.admins.functions import create_admin
import click
from werkzeug.security import generate_password_hash
from datetime import datetime


app = create_app()


@click.group()
def cli():
    pass


@click.command('create-db')
def create_db():
    app.app_context().push()
    db.create_all()
    print('All tables created')


@click.command('drop-db')
def drop_db():
    app.app_context().push()
    db.drop_all()
    print('All tables deleted')


@click.command('create-admin')
def create_admin_command():
    app.app_context().push()

    name = input('Name: ')
    email = input('Email: ')
    password = input('Password: ')
    confirm = input('Confirm password: ')

    if name and email and password and confirm:
        if email_unique_validation(email, ''):
            if email_regex_validation(email):
                if password == confirm:
                    password = generate_password_hash(password, method='sha256')
                    create_user(name, email, password)
                    user_id = Users.query.filter_by(email=email).one().id
                    create_admin(user_id)
                    print('Admin user created')
                else:
                    print('Password mismatch')
            else:
                print('Email regex check failed')
        else:
            print('Email address already exists')


@click.command('load-test-data')
def load_test_data():
    app.app_context().push()

    password = generate_password_hash('test')
    create_user('Borya', 'Borya@email.com', password)
    create_user('Slava', 'Slava@email.com', password)
    create_user('Petya', 'Petya@email.com', password)
    create_user('Dima', 'Dima@email.com', password)
    create_user('Ilya', 'Ilya@email.com', password)

    create_city('Washington')
    create_city('Paris')
    create_city('Tokyo')
    create_city('London')
    create_city('Moscow')

    create_topic('Food')
    create_topic('Art')
    create_topic('Science')
    create_topic('Sport')
    create_topic('It')

    description = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. " \
                  "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, " \
                  "when an unknown printer took a galley of type and scrambled it to make a type specimen book. " \
                  "It has survived not only five centuries, but also the leap into electronic typesetting, " \
                  "remaining essentially unchanged. " \
                  "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, " \
                  "and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

    start0 = datetime.strptime('2021-06-01 12:00', "%Y-%m-%d %H:%M")
    start1 = datetime.strptime('2021-06-02 12:00', "%Y-%m-%d %H:%M")
    start2 = datetime.strptime('2021-06-03 12:00', "%Y-%m-%d %H:%M")
    start3 = datetime.strptime('2021-06-04 12:00', "%Y-%m-%d %H:%M")
    start4 = datetime.strptime('2021-06-05 12:00', "%Y-%m-%d %H:%M")

    end0 = datetime.strptime('2021-06-03 18:00', "%Y-%m-%d %H:%M")
    end1 = datetime.strptime('2021-06-04 18:00', "%Y-%m-%d %H:%M")
    end2 = datetime.strptime('2021-06-05 18:00', "%Y-%m-%d %H:%M")
    end3 = datetime.strptime('2021-06-06 18:00', "%Y-%m-%d %H:%M")
    end4 = datetime.strptime('2021-06-07 18:00', "%Y-%m-%d %H:%M")

    create_event('Pizza festival', description, start0, end0, 1, 1)
    create_event('Art exhibition', description, start1, end1, 2, 2)
    create_event('Science exhibition', description, start2, end2, 3, 3)
    create_event('Football match', description, start3, end3, 4, 4)
    create_event('It conference', description, start4, end4, 5, 5)


cli.add_command(create_db)
cli.add_command(drop_db)
cli.add_command(create_admin_command)
cli.add_command(load_test_data)


if __name__ == '__main__':
    cli()
