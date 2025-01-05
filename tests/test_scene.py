"""Tests for the Scene object."""

from netflix_vfx_naming import Scene


def test_scene_creation_has_correct_defaults(scene: Scene.Scene) -> None:
    """Test Scene creation defaults."""
    assert scene.name == "default_scene"
    assert scene.desc == "default scene description"
