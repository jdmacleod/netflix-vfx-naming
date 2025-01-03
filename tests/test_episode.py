"""Tests for the narrative_objects package."""

import pytest

from netflix_vfx_naming import Episode


def test_episode_creation_has_defaults(episode: Episode) -> None:
    """Test Episode creation defaults."""
    assert episode.name == "default_episode"
    assert episode.desc == "default episode description"
