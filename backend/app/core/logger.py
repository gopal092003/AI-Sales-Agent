import sys

from loguru import logger

from app.core.config import settings
from app.core.constants import LOG_FORMAT


def setup_logger():
    """
    Configure and return application logger.
    """

    # Remove default logger
    logger.remove()

    # Console logger
    logger.add(
        sys.stdout,
        format=LOG_FORMAT,
        level=settings.LOG_LEVEL,
        colorize=True,
        backtrace=True,
        diagnose=True if settings.DEBUG else False,
    )

    return logger