import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "makaton_app.log"


def setup_logging() -> logging.Logger:
    """
    Configure application-wide logging.

    - Logs to console and to logs/makaton_app.log
    - Uses a rotating file handler to avoid unbounded log size
    """
    root_logger = logging.getLogger()

    # Avoid adding handlers twice if setup_logging is called multiple times
    if root_logger.handlers:
        return root_logger

    root_logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=1_000_000,  # ~1 MB per file
        backupCount=3,  # keep last 3 log files
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    return root_logger
