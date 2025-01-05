"""Tests for the package logging setup."""

import pytest

from netflix_vfx_naming import logger


def test_basic_logging_levels(caplog: pytest.LogCaptureFixture) -> None:
    """Test basic logging levels.

    Args:
        caplog (obj): standard pytest fixture.
    """
    logger.warning("This is a warning message.")
    assert "This is a warning message." in caplog.text

    logger.error("This is an error message.")
    assert "This is an error message." in caplog.text

    logger.critical("This is a critical message.")
    assert "This is a critical message." in caplog.text
