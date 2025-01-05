"""Tests for the Sequence object."""

from netflix_vfx_naming import Sequence


def test_sequence_creation_has_correct_defaults(sequence: Sequence.Sequence) -> None:
    """Test Season creation defaults."""
    assert sequence.name == "default_sequence"
    assert sequence.desc == "default sequence description"
