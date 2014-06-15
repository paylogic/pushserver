"""Test stream view."""
from flask.ext.sse import send_event


def test_stream_view(server, http):
    """"Test stream view."""
    response = http.get("/stream?channel='test'")
    assert response.is_streamed
    assert response.content_type == 'text/event-stream; charset=utf-8'

    with server.app_context():
        send_event('myevent', '1', channel='test')
