"""Tests for the narrative_objects package."""

import pytest

from netflix_vfx_naming import Season


def test_season_creation_has_defaults(season: Season) -> None:
    """Test Season creation defaults."""
    assert season.name == "default_season"
    assert season.desc == "default season description"
