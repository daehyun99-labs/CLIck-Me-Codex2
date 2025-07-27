"""로깅 설정 유틸리티."""

import logging
from logging import Logger


def get_logger(name: str) -> Logger:
    """기본 설정이 적용된 :class:`Logger` 객체를 반환합니다."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
