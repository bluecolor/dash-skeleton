from sqlalchemy.event import listens_for

from .base import db, Column

class TimestampMixin(object):
    updated_at = Column(db.DateTime(True), default=db.func.now(), nullable=False)
    created_at = Column(db.DateTime(True), default=db.func.now(), nullable=False)

@listens_for(TimestampMixin, "before_update", propagate=True)
def timestamp_before_update(mapper, connection, target):
    # Check if we really want to update the updated_at value
    if hasattr(target, "skip_updated_at"):
        return

    target.updated_at = db.func.now()
