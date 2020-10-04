import time

from flask.cli import AppGroup
from sqlalchemy.exc import DatabaseError
import sqlalchemy
from flask_migrate import stamp

manager = AppGroup(help="Manage the database (create/drop tables. reencrypt data.).")

def _wait_for_db_connection(db):
    retried = False
    while not retried:
        try:
            db.engine.execute("SELECT 1;")
            return
        except DatabaseError:
            time.sleep(30)

        retried = True

@manager.command()
def create_tables():
    """Create the database tables."""
    from app.models import db

    _wait_for_db_connection(db)
    # To create triggers for searchable models, we need to call configure_mappers().
    sqlalchemy.orm.configure_mappers()
    db.create_all()

    # Need to mark current DB as up to date
    stamp()

@manager.command()
def drop_tables():
    """Drop the database tables."""
    from app.models import db
    _wait_for_db_connection(db)
    db.drop_all()

