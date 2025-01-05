"""Tests relationships for the Season."""

from netflix_vfx_naming import Episode, Season, Show


def test_season_can_add_child_episode(
    season: Season.Season, episode: Episode.Episode
) -> None:
    """Test adding a child Episode to a Season."""
    season.add_child(episode)
    assert len(season.children) == 1
    assert episode.parent == season


def test_season_can_remove_child_episode(
    season: Season.Season, episode: Episode.Episode
) -> None:
    """Test adding then removing a child Episode from a Season."""
    season.add_child(episode)
    assert len(season.children) == 1

    season.remove_child(episode)
    assert len(season.children) == 0
    assert episode.parent is None


def test_season_can_set_parent_show(season: Season.Season, show: Show.Show) -> None:
    """Test setting a parent Show for a Season."""
    season.set_parent(show)
    assert season.parent == show
    assert len(show.children) == 1
