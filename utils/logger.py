import logging
from utils.constants import LOG_FORMAT, LOG_LEVEL


def get_logger(name: str):
    """
    Create and return configured logger.
    """

    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(LOG_FORMAT)
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(LOG_LEVEL)

    return logger
