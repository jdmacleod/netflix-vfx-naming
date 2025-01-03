"""Tests for the narrative_objects package."""

import pytest

from netflix_vfx_naming import Scene


def test_scene_creation_has_defaults(scene: Scene) -> None:
    """Test Scene creation defaults."""
    assert scene.name == "default_scene"
    assert scene.desc == "default scene description"
