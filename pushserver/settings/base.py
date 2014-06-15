"""Pushserver base configuration.
"""


class Config(object):
    """Base Configuration.

    This should contain default values that will be used by all environments.

    """
    DEBUG = False
    TESTING = False
    SERVER_NAME = None
    SENTRY_DSN = None

    BLUEPRINTS = (
        ('flask.ext.sse.sse', '/stream'),
    )
    SSE_REDIS_HOST = 'localhost'
    SSE_REDIS_PORT = 6379
    SSE_REDIS_DB = 0
