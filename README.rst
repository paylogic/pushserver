pushserver
==========

Simple but powerful HTML5 Server-Sent Events (SSE) server for any kind of updates coming from the backend to the client
This app is the integration of the `Flask-SSE <https://github.com/DazWorrall/flask-sse>`_ into a simple generic flask
app.
Refer to flask-sse docs for more info about the applicable settings.


Development Environment
-----------------------

To set up the development environment, run:

::

    make develop


Running the development instance
--------------------------------

::

    env/bin/python manage.py runserver

You can access your push server via http://localhost:8080/stream


Production deployment
---------------------

As you need a non-blocking server, it's recommended to use `gunicorn <http://gunicorn.org/>`_ + `gevent <gevent.org>`_
or just gevent wsgi server:

::

    gunicorn -k gevent wsgi:app



Sending events to a push server from your app
---------------------------------------------

::

    import json

    from flask.ext.sse import sse, send_event

    send_event('myevent', json.dumps({"message": "Hello!"}))


Client side
-----------

On the client side you just need a javascipt handler function which will be called when a new message is pushed from the server.

::

    var source = new EventSource('/stream');
    source.onmessage = function (event) {
         alert(event.data);
    };

Server-Sent Events are supported by recent Firefox, Chrome and Safari browsers.
Internet Explorer does not yet support Server-Sent Events, but is expected to support them in Version 10.
There are two recommended Polyfills to support older browsers

* EventSource.js
* jquery.eventsource


Contact
-------

If you have questions, bug reports, suggestions, etc. please create an issue on
the `GitHub project page <http://github.com/paylogic/pushserver>`_.


License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

See `License <https://github.com/paylogic/pushserver/blob/master/LICENSE.txt>`_


© 2014 Paylogic International.
