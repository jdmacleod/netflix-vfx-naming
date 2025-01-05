"""Helper module for VFX naming, after Netflix Partner recommendations."""

import logging
import os

# set up logging
logger = logging.getLogger(__name__)
if logger.handlers:
    console_handler = logger.handlers[0]
else:
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)

basic_formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_handler.setFormatter(basic_formatter)
console_handler.setLevel(logging.INFO)

# permit env var configuration of logging
env_log_level = os.getenv("PYTHON_LOG_LEVEL")

if env_log_level:
    try:
        logger.setLevel(env_log_level.upper())
        logger.info(
            f"honored environment PYTHON_LOG_LEVEL value of '{env_log_level}', logging level set to {env_log_level.upper()}."
        )
        # configure debug logging with additional details
        if env_log_level.upper() == "DEBUG":
            if logger.handlers:
                console_handler = logger.handlers[0]
            else:
                console_handler = logging.StreamHandler()
                logger.addHandler(console_handler)
            debug_formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(filename)s - L%(lineno)d - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
            console_handler.setFormatter(debug_formatter)
            logger.info(
                f"honored environment PYTHON_LOG_LEVEL value of '{env_log_level}', debug logging enabled."
            )
    except BaseException as e:
        logger.warning(
            f"ignored unmappable environment PYTHON_LOG_LEVEL value of '{env_log_level}', leaving current logging level of {logger.getEffectiveLevel()} unchanged. {e}"
        )
