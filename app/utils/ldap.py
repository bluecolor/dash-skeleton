import logging
import ldap
from sqlalchemy.orm.exc import NoResultFound

from app import settings
from app import models

logger = logging.getLogger("util.ldap")


def auth_user(username, password):
    if not password:
        return None
    try:
        client = ldap.initialize(settings.LDAP_URL)
        client.simple_bind_s(settings.LDAP_USERNAME, settings.LDAP_PASSWORD)

        query = settings.LDAP_QUERY % username
        result = client.search_s(
            settings.LDAP_BASE_DN, ldap.SCOPE_SUBTREE, query)

        if len(result) == 0:
            return None

        user, props = result.pop()
        client.simple_bind_s(user, password)
        client.unbind_s()

        groups = "`".join([dict(kv.split('=') for kv in p.decode('utf-8').split(',')
               if kv.split('=')[0] == 'CN')['CN'].strip() for p in props.get('memberOf')])

        # authenticated
        # check user in db and create it if not exists
        try:
            # find user and update groups
            user = models.User.find_by_username(username)
            user.groups = groups
            models.db.session.commit()
            return user
        except NoResultFound:
            logger.info("New user, creating ...")

        if props.get(settings.LDAP_PROP_EMAIL):
            email = props.get(settings.LDAP_PROP_EMAIL).pop().decode("utf-8")
        else:
            email = None

        user = models.User(name=username, username=username, email=email, groups=groups)
        models.db.session.add(user)
        models.db.session.commit()
        return user

    except ldap.LDAPError as e:
        logger.error(e)
        return None
