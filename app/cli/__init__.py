import click
from flask.cli import FlaskGroup, run_command
from flask import current_app

from app import __version__, create_app, settings
from app.cli import database, user

def create(group):
    app = current_app or create_app()
    group.app = app

    @app.shell_context_processor
    def shell_context():
        return {"settings": settings}

    return app

@click.group(cls=FlaskGroup, create_app=create)
def manager():
    """Management script for App"""


manager.add_command(run_command, "runserver")
manager.add_command(database.manager, "database")
manager.add_command(user.manager, "user")