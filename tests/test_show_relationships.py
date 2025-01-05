"""Tests relationships for the Show."""

from netflix_vfx_naming import Episode, Scene, Season, Sequence, Show


def test_show_can_add_child_sequence(
    show: Show.Show, sequence: Sequence.Sequence
) -> None:
    """Test adding a child Sequence to a Show."""
    show.add_child(sequence)
    assert len(show.children) == 1
    assert sequence.parent == show


def test_show_can_remove_child_sequence(
    show: Show.Show, sequence: Sequence.Sequence
) -> None:
    """Test adding then removing a child Sequence from a Show."""
    show.add_child(sequence)
    assert len(show.children) == 1

    show.remove_child(sequence)
    assert len(show.children) == 0
    assert sequence.parent is None


def test_show_can_add_child_scene(show: Show.Show, scene: Scene.Scene) -> None:
    """Test adding a child Scene to a Show."""
    show.add_child(scene)
    assert len(show.children) == 1
    assert scene.parent == show


def test_show_can_remove_child_scene(show: Show.Show, scene: Scene.Scene) -> None:
    """Test adding then removing a child Scene from a Show."""
    show.add_child(scene)
    assert len(show.children) == 1

    show.remove_child(scene)
    assert len(show.children) == 0
    assert scene.parent is None


def test_show_can_add_child_episode(show: Show.Show, episode: Episode.Episode) -> None:
    """Test adding a child Episode to a Show."""
    show.add_child(episode)
    assert len(show.children) == 1
    assert episode.parent == show


def test_show_can_remove_child_episode(
    show: Show.Show, episode: Episode.Episode
) -> None:
    """Test adding then removing a child Episode from a Show."""
    show.add_child(episode)
    assert len(show.children) == 1

    show.remove_child(episode)
    assert len(show.children) == 0
    assert episode.parent is None


def test_show_can_add_child_season(show: Show.Show, season: Season.Season) -> None:
    """Test adding a child Season to a Show."""
    show.add_child(season)
    assert len(show.children) == 1
    assert season.parent == show


def test_show_can_remove_child_season(show: Show.Show, season: Season.Season) -> None:
    """Test adding then removing a child Season from a Show."""
    show.add_child(season)
    assert len(show.children) == 1

    show.remove_child(season)
    assert len(show.children) == 0
    assert season.parent is None
