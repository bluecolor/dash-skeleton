import logging
import uuid

logger = logging.getLogger("pages.registery")


class Registery:
    def __init__(self):
        self.__registery = dict()

    def register(self, page):
        if page.get("id") is None:
            logger.warn("Page doesnot have id setting one")
            page["id"] = page.get("id", str(uuid.uuid4()))

        if page.get("enabled", True):
            logger.debug("Registering %s page.", page["id"])
            if self.__registery.get(page["id"]) is not None:
                raise ValueError(
                    f"""Name {page["id"]} with page already registered.
                        pages codes must be unique!
                    """
                )
            self.__registery[page["id"]] = page
        else:
            logger.debug(
                """%s page is not enabled, not registering.""", page["id"],
            )

    def get(self, name):
        print(self.__registery)
        return self.__registery.get(name)

    @property
    def pages(self):
        return self.__registery.values()

    @property
    def items(self):
        return self.__registery
