"""Pushserver test config."""
import pytest

from pushserver.server import create_app


@pytest.fixture(scope='session')
def server():
    """Flask application object."""
    return create_app(mode='development')


@pytest.fixture
def http(server):
    """Test client.

    Usage:
        with http as c:
            response = c.get(uri)
            print response.parsed_data
    """
    client = server.test_client()
    return client
