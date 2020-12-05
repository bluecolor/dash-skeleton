from enum import unique
from functools import reduce
import logging
import hashlib

from flask_login import UserMixin
from sqlalchemy_utils.models import generic_repr
from sqlalchemy_utils import EmailType
from sqlalchemy.orm.exc import NoResultFound
from passlib.apps import custom_app_context as pwd_context

from .base import db, Column
from .mixins import TimestampMixin


logger = logging.getLogger(__name__)

@generic_repr("id", "name", "email")
class User(
    TimestampMixin, db.Model, UserMixin
):
    __tablename__ = "users"

    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(320), unique=True)
    name = Column(db.String(320))
    email = Column(EmailType, nullable=True)
    password_hash = Column(db.String(128), nullable=True)

    def __str__(self):
        return "%s (%s)" % (self.name, self.email)

    def __init__(self, *args, **kwargs):
        if kwargs.get("email") is not None:
            kwargs["email"] = kwargs["email"].lower()
        super(User, self).__init__(*args, **kwargs)


    def to_dict(self):
        d = {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "email": self.email,
        }

        return d


    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.filter(cls.id == user_id).one()

    @classmethod
    def is_user_exists(cls, email):
        try:
            user = cls.get_by_email(email)
            return user is not None
        except NoResultFound:
            return False

    @classmethod
    def all(cls):
        return cls.query.filter(cls.disabled_at.is_(None))

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter(cls.email == email)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter(cls.username == username).one()

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return self.password_hash and pwd_context.verify(password, self.password_hash)

    def get_id(self):
        identity = hashlib.md5(
            "{},{}".format(self.email, self.password_hash).encode()
        ).hexdigest()
        return "{0}-{1}".format(self.id, identity)
