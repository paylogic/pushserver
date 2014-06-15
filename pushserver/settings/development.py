"""Pushserver development configuration.
"""
import logging

from .base import Config as BaseConfig


class Config(BaseConfig):
    """Configuration for the Development environment."""
    DEBUG = True
    PORT = 8080
    HOST = '127.0.0.1'
    SERVER_NAME = '{0}:{1}'.format(HOST, PORT)
    LOGFILE = logging.handlers.SysLogHandler.LOG_LOCAL4
