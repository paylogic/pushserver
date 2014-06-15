#!/usr/bin/env python

from pushserver.server import create_app
from flask.ext.script import Manager, Server, Shell


httpapi_app = create_app(mode='development')
manager = Manager(httpapi_app)
manager.add_command('shell', Shell())
manager.add_command(
    'runserver',
    Server(
        host=httpapi_app.config['HOST'],
        port=httpapi_app.config['PORT'],
        use_debugger=httpapi_app.config['DEBUG'],
        threaded=True,
    )
)

if __name__ == "__main__":
    manager.run()
