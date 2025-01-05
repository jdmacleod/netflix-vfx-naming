"""Tests relationships for the Scene."""

from netflix_vfx_naming import Episode, Scene, Sequence, Shot, Show


def test_scene_can_add_child_shot(scene: Scene.Scene, shot: Shot.Shot) -> None:
    """Test adding a child Shot to a Scene."""
    scene.add_child(shot)
    assert len(scene.children) == 1
    assert shot.parent == scene


def test_scene_can_remove_child_shot(scene: Scene.Scene, shot: Shot.Shot) -> None:
    """Test adding then removing a child Shot to a Scene."""
    scene.add_child(shot)
    assert len(scene.children) == 1

    scene.remove_child(shot)
    assert len(scene.children) == 0
    assert shot.parent is None


def test_scene_can_set_parent_sequence(
    scene: Scene.Scene, sequence: Sequence.Sequence
) -> None:
    """Test setting a parent Sequence for a Scene."""
    scene.set_parent(sequence)
    assert scene.parent == sequence
    assert len(sequence.children) == 1


def test_scene_can_set_parent_episode(
    scene: Scene.Scene, episode: Episode.Episode
) -> None:
    """Test setting a parent Episode for a Scene."""
    scene.set_parent(episode)
    assert scene.parent == episode
    assert len(episode.children) == 1


def test_episode_can_set_parent_show(scene: Scene.Scene, show: Show.Show) -> None:
    """Test setting a parent Show for a Scene."""
    scene.set_parent(show)
    assert scene.parent == show
    assert len(show.children) == 1
