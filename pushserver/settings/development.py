"""Pushserver development configuration.
"""
import logging.handlers

from pushserver.settings.base import Config as BaseConfig


class Config(BaseConfig):
    """Configuration for the Development environment."""
    DEBUG = True
    PORT = 8080
    HOST = '127.0.0.1'
    LOGFILE = logging.handlers.SysLogHandler.LOG_LOCAL4
