import uuid
from inflection import dasherize, humanize


class Page():

    PAGE_ID = None

    @classmethod
    def code(cls):
        if cls.PAGE_ID is None:
            cls.PAGE_ID = str(uuid.uuid4())
        return  dasherize(cls.__name__.lower() + "-" + cls.PAGE_ID)

    @classmethod
    def name(cls):
        return humanize(cls.__name__)

    @classmethod
    def enabled(cls):
        return True

    @classmethod
    def render(cls):
        raise NotImplementedError()
