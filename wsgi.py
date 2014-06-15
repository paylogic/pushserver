"""WSGI script for the pushserver application."""
from pushserver.server import create_app
app = create_app(mode='development')
