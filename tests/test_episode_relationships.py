"""Tests relationships for the Episode."""

from netflix_vfx_naming import Episode, Scene, Season, Sequence, Show


def test_episode_can_add_child_sequence(
    episode: Episode.Episode, sequence: Sequence.Sequence
) -> None:
    """Test adding a child Sequence to an Episode."""
    episode.add_child(sequence)
    assert len(episode.children) == 1
    assert sequence.parent == episode


def test_episode_can_remove_child_sequence(
    episode: Episode.Episode, sequence: Sequence.Sequence
) -> None:
    """Test adding then removing a child Sequence from an Episode."""
    episode.add_child(sequence)
    assert len(episode.children) == 1

    episode.remove_child(sequence)
    assert len(episode.children) == 0
    assert sequence.parent is None


def test_episode_can_add_child_scene(
    episode: Episode.Episode, scene: Scene.Scene
) -> None:
    """Test adding a child Scene to an Episode."""
    episode.add_child(scene)
    assert len(episode.children) == 1
    assert scene.parent == episode


def test_episode_can_remove_child_scene(
    episode: Episode.Episode, scene: Scene.Scene
) -> None:
    """Test adding then removing a child Scene from an Episode."""
    episode.add_child(scene)
    assert len(episode.children) == 1

    episode.remove_child(scene)
    assert len(episode.children) == 0
    assert scene.parent is None


def test_episode_can_set_parent_season(
    episode: Episode.Episode, season: Season.Season
) -> None:
    """Test setting a parent Season for an Episode."""
    episode.set_parent(season)
    assert episode.parent == season
    assert len(season.children) == 1


def test_episode_can_set_parent_show(episode: Episode.Episode, show: Show.Show) -> None:
    """Test setting a parent Show for an Episode."""
    episode.set_parent(show)
    assert episode.parent == show
    assert len(show.children) == 1
