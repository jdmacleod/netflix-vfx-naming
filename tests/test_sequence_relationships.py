"""Tests relationships for the Sequence."""

from netflix_vfx_naming import Episode, Scene, Sequence, Shot, Show


def test_sequence_can_add_child_shot(
    sequence: Sequence.Sequence, shot: Shot.Shot
) -> None:
    """Test adding a child Shot to a Sequence."""
    sequence.add_child(shot)
    assert len(sequence.children) == 1
    assert shot.parent == sequence


def test_sequence_can_remove_child_shot(
    sequence: Sequence.Sequence, shot: Shot.Shot
) -> None:
    """Test adding then removing a child Shot from a Sequence."""
    sequence.add_child(shot)
    assert len(sequence.children) == 1

    sequence.remove_child(shot)
    assert len(sequence.children) == 0
    assert shot.parent is None


def test_sequence_can_add_child_scene(
    sequence: Sequence.Sequence, scene: Scene.Scene
) -> None:
    """Test adding a child Scene to a Sequence."""
    sequence.add_child(scene)
    assert len(sequence.children) == 1
    assert scene.parent == sequence


def test_sequence_can_remove_child_scene(
    sequence: Sequence.Sequence, scene: Scene.Scene
) -> None:
    """Test adding then removing a child Scene from a Sequence."""
    sequence.add_child(scene)
    assert len(sequence.children) == 1

    sequence.remove_child(scene)
    assert len(sequence.children) == 0
    assert scene.parent is None


def test_sequence_can_set_parent_episode(
    sequence: Sequence.Sequence, episode: Episode.Episode
) -> None:
    """Test setting a parent Episode for a Sequence."""
    sequence.set_parent(episode)
    assert sequence.parent == episode
    assert len(episode.children) == 1


def test_sequence_can_set_parent_show(
    sequence: Sequence.Sequence, show: Show.Show
) -> None:
    """Test setting a parent Show for a Sequence."""
    sequence.set_parent(show)
    assert sequence.parent == show
    assert len(show.children) == 1
