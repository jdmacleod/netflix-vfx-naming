"""Tests relationships for the Shot."""

from netflix_vfx_naming import Scene, Sequence, Shot


def test_shot_can_set_parent_scene(shot: Shot.Shot, scene: Scene.Scene) -> None:
    """Test setting a parent Scene for a Shot."""
    shot.set_parent(scene)
    assert shot.parent == scene
    assert len(scene.children) == 1


def test_shot_can_set_parent_sequence(
    shot: Shot.Shot, sequence: Sequence.Sequence
) -> None:
    """Test setting a parent Sequence for a Shot."""
    shot.set_parent(sequence)
    assert shot.parent == sequence
    assert len(sequence.children) == 1
