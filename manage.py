#!/usr/bin/env python

from pushserver.server import create_app
from flask.ext.script import Manager, Server, Shell

app = create_app(mode='development')
manager = Manager(app)
manager.add_command('shell', Shell())
manager.add_command(
    'runserver',
    Server(
        host=app.config['HOST'],
        port=app.config['PORT'],
        use_debugger=app.config['DEBUG'],
        threaded=True,
    )
)

if __name__ == "__main__":
    manager.run()
