"""Tests for the narrative_objects package."""

import pytest

from netflix_vfx_naming import Sequence


def test_sequence_creation_has_defaults(sequence: Sequence) -> None:
    """Test Season creation defaults."""
    assert sequence.name == "default_sequence"
    assert sequence.desc == "default sequence description"
