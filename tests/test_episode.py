"""Tests for the Episode object."""

from netflix_vfx_naming import Episode


def test_episode_creation_has_correct_defaults(episode: Episode.Episode) -> None:
    """Test Episode creation defaults."""
    assert episode.name == "default_episode"
    assert episode.desc == "default episode description"
