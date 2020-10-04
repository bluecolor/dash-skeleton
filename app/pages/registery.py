import logging

logger = logging.getLogger("pages.registery")


class Registery:
    def __init__(self):
        self.__registery = dict()

    def register(self, page):
        if page.enabled():
            logger.debug("Registering %s page.", page.code())
            if self.__registery.get(page.code()) is not None:
                raise ValueError(
                    f"""Name {page.code()} with page already registered.
                        pages codes must be unique!
                    """
                )
            self.__registery[page.code()] = page
        else:
            logger.debug(
                """%s page is not enabled, not registering.""", page.code(),
            )

    def get(self, name):
        return self.__registery.get(name)

    @property
    def pages(self):
        return self.__registery.values()

    @property
    def items(self):
        return self.__registery
