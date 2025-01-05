"""Tests for the Shot object."""

from netflix_vfx_naming import Episode, Scene, Sequence, Shot, Show


def test_shot_creation_has_correct_defaults(shot: Shot.Shot) -> None:
    """Test Shot creation defaults."""
    assert shot.name == "default_shot"
    assert shot.desc == "default shot description"


def test_shot_fullname_is_correct(
    shot: Shot.Shot,
    scene: Scene.Scene,
    sequence: Sequence.Sequence,
    episode: Episode.Episode,
    show: Show.Show,
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
    shot.set_parent(scene)
    scene.set_parent(episode)
    episode.set_parent(show)

    fullname = shot.get_fullname()
    assert fullname == "AGM_104_065_010"

    # Episodic that does not use scenes
    shot.set_parent(sequence)
    sequence.set_parent(episode)
    episode.set_parent(show)

    fullname = shot.get_fullname()
    assert fullname == "AGM_104_TCC_010"

    # Episodic that uses scenes and sequences
    shot.set_parent(scene)
    scene.set_parent(sequence)
    sequence.set_parent(episode)
    episode.set_parent(show)

    fullname = shot.get_fullname()
    assert fullname == "AGM_104_TCC_065_010"

    # Feature that does not use sequences
    shot.set_parent(scene)
    scene.set_parent(show)

    fullname = shot.get_fullname()
    assert fullname == "AGM_065_010"

    # Feature that does not use scenes
    shot.set_parent(sequence)
    sequence.set_parent(show)

    fullname = shot.get_fullname()
    assert fullname == "AGM_TCC_010"

    # Feature that uses scenes and sequences
    shot.set_parent(scene)
    scene.set_parent(sequence)
    sequence.set_parent(show)

    fullname = shot.get_fullname()
    assert fullname == "AGM_TCC_065_010"
