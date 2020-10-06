import functools
from flask_sqlalchemy import BaseQuery, SQLAlchemy
from sqlalchemy.pool import NullPool
# from sqlalchemy_searchable import make_searchable

from app import settings
from app.utils import json_dumps

class AppSQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        options.update(json_serializer=json_dumps)
        if settings.SQLALCHEMY_ENABLE_POOL_PRE_PING:
            options.update(pool_pre_ping=True)
        super(AppSQLAlchemy, self).apply_driver_hacks(app, info, options)

    def apply_pool_defaults(self, app, options):
        super(AppSQLAlchemy, self).apply_pool_defaults(app, options)
        if settings.SQLALCHEMY_ENABLE_POOL_PRE_PING:
            options["pool_pre_ping"] = True
        if settings.SQLALCHEMY_DISABLE_POOL:
            options["poolclass"] = NullPool
            # Remove options NullPool does not support:
            options.pop("max_overflow", None)


db = AppSQLAlchemy(session_options={"expire_on_commit": False})
# Make sure the SQLAlchemy mappers are all properly configured first.
# This is required by SQLAlchemy-Searchable as it adds DDL listeners
# on the configuration phase of models.
db.configure_mappers()

# listen to a few database events to set up functions, trigger updates
# and indexes for the full text search
# make_searchable(db.metadata, options={"regconfig": "pg_catalog.simple"})

Column = functools.partial(db.Column, nullable=False)



