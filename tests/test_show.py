"""Tests for the narrative_objects package."""

import pytest

from netflix_vfx_naming import Show


def test_shot_creation_has_defaults(show: Show) -> None:
    """Test Show creation defaults."""
    assert show.name == "default_show"
    assert show.desc == "default show description"
