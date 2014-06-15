"""Pushserver Flask application."""
import logging.handlers
import os
import sys
from raven.handlers.logging import SentryHandler
from flask import Flask

from werkzeug.utils import import_string


def create_app(name=__name__, mode='development', config=None):
    """Create and initialize the application."""
    app = Flask(name)

    # Load the configuration
    mode = mode.lower()

    try:
        app.config.from_object(
            u'pushserver.settings.{0}.Config'.format(mode)
        )
        if config and os.path.exist(config):
            app.config.from_file(config)
    except ImportError:
            raise RuntimeError("Can't find Config in pushserver.settings.{0}"
                               .format(mode))

    # Setup Logging
    logger = logging.getLogger('pushserver')

    if app.config['SENTRY_DSN']:
        handler = SentryHandler(app.config['SENTRY_DSN'], level=logging.ERROR)
        logger.addHandler(handler)

    address = '/var/run/syslog' if sys.platform == 'darwin' else '/dev/log'
    syslog = logging.handlers.SysLogHandler(
        facility=app.config['LOGFILE'],
        address=address,
    )
    logger.addHandler(syslog)
    syslog.setLevel(logging.INFO)
    app.logger.addHandler(logger)

    # Setup endpoints (blueprints)
    load_blueprints(app)

    return app


def load_blueprints(app):
    """Load the blueprints from the configuration."""
    for app_location, url_prefix in app.config['BLUEPRINTS']:
        app_blueprint = import_string(app_location)
        app.register_blueprint(app_blueprint, url_prefix=url_prefix)
