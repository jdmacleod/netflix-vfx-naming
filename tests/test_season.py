"""Tests for the Season object."""

from netflix_vfx_naming import Season


def test_season_creation_has_correct_defaults(season: Season.Season) -> None:
    """Test Season creation defaults."""
    assert season.name == "default_season"
    assert season.desc == "default season description"
