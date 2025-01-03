"""Tests for the narrative_objects package."""

import pytest

from netflix_vfx_naming import Episode, Scene, Sequence, Shot, Show


def test_shot_creation_has_defaults(shot: Shot) -> None:
    """Test Shot creation defaults."""
    assert shot.name == "default_shot"
    assert shot.desc == "default shot description"


def test_shot_fullname_is_correct(
    shot: Shot, scene: Scene, sequence: Sequence, episode: Episode, show: Show
) -> None:
    """Test Shot fullname construction."""
    fullname = shot.get_fullname()

    assert fullname == shot.name

    show.name = "AGM"
    episode.name = "104"
    sequence.name = "TCC"
    scene.name = "065"
    shot.name = "010"

    # Episodic that does not use sequences
    shot.parent = scene
    scene.parent = episode
    episode.parent = show

    fullname = shot.get_fullname()
    assert fullname == "AGM_104_065_010"

    # Episodic that does not use scenes
    shot.parent = sequence
    sequence.parent = episode
    episode.parent = show

    fullname = shot.get_fullname()
    assert fullname == "AGM_104_TCC_010"

    # Episodic that uses scenes and sequences
    shot.parent = scene
    scene.parent = sequence
    sequence.parent = episode
    episode.parent = show

    fullname = shot.get_fullname()
    assert fullname == "AGM_104_TCC_065_010"

    # Feature that does not use sequences
    shot.parent = scene
    scene.parent = show

    fullname = shot.get_fullname()
    assert fullname == "AGM_065_010"

    # Feature that does not use scenes
    shot.parent = sequence
    sequence.parent = show

    fullname = shot.get_fullname()
    assert fullname == "AGM_TCC_010"

    # Feature that uses scenes and sequences
    shot.parent = scene
    scene.parent = sequence
    sequence.parent = show

    fullname = shot.get_fullname()
    assert fullname == "AGM_TCC_065_010"
