"""Tests for the Show object."""

from netflix_vfx_naming import Show


def test_shot_creation_has_correct_defaults(show: Show.Show) -> None:
    """Test Show creation defaults."""
    assert show.name == "default_show"
    assert show.desc == "default show description"
