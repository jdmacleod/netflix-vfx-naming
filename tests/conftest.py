"""Pytest configuration and fixtures."""

import pytest

from netflix_vfx_naming import Episode, Scene, Season, Sequence, Shot, Show


@pytest.fixture
def episode() -> Episode.Episode:
    """Provide a fresh episode instance for each test."""
    return Episode.Episode()


@pytest.fixture
def scene() -> Scene.Scene:
    """Provide a fresh scene instance for each test."""
    return Scene.Scene()


@pytest.fixture
def season() -> Season.Season:
    """Provide a fresh season instance for each test."""
    return Season.Season()


@pytest.fixture
def sequence() -> Sequence.Sequence:
    """Provide a fresh sequence instance for each test."""
    return Sequence.Sequence()


@pytest.fixture
def shot() -> Shot.Shot:
    """Provide a fresh shot instance for each test."""
    return Shot.Shot()


@pytest.fixture
def show() -> Show.Show:
    """Provide a fresh show instance for each test."""
    return Show.Show()
