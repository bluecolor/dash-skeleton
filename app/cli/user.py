import click
from flask.cli import AppGroup
from sqlalchemy.orm.exc import NoResultFound
from app import models
from .database import _wait_for_db_connection

manager = AppGroup(help="Manage the users")


@manager.command()
@click.argument('name', nargs=1)
@click.argument('email', nargs=1)
@click.argument('password', nargs=1)
def create(name, email, password):
    """Create user"""
    _wait_for_db_connection(models.db)

    try:
        user = models.User.get_by_email(email)
        if user is not None:
            raise ValueError("Email already exists")
    except NoResultFound:
        pass

    user = models.User(name=name, email=email)
    user.hash_password(password)
    models.db.session.add(user)
    models.db.session.commit()


@manager.command()
@click.argument('email', nargs=1)
def delete(email):
    """Delete user"""
    _wait_for_db_connection(models.db)

    try:
        user = models.User.get_by_email(email)
    except NoResultFound:
        raise ValueError("Email not found")

    models.db.session.delete(user)
    models.db.session.commit()


@manager.command()
@click.argument('email', nargs=1)
@click.argument('password', nargs=1)
def password(email):
    """Delete user"""
    _wait_for_db_connection(models.db)

    try:
        user = models.User.get_by_email(email)
        user.hash_password(password)
    except NoResultFound:
        raise ValueError("Email not found")

    models.db.session.commit()
