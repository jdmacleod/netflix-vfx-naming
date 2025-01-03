"""Sequence class."""
import typing
from typing import List, Union

from netflix_vfx_naming import Base, Episode, Scene, Shot, Show


class Sequence(Base.Base):
    """Sequence narrative object."""

    def __init__(self) -> None:
        """Initialize sequence narrative object."""
        super().__init__()
        print("init Sequence")
        self.name = "default_sequence"
        self.desc = "default sequence description"
        self.parent: typing.Optional[Union[Show.Show, Episode.Episode]] = None
        self.children: typing.Optional[Union[List[Scene.Scene], List[Shot.Shot]]] = None
