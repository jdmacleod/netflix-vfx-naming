"""Sequence class."""
import typing
from typing import List, Union

from netflix_vfx_naming import Base, Episode, Scene, Shot, Show


class Sequence(Base.Base):
    """Sequence narrative object."""

    def __init__(
        self, name: str = "default_sequence", desc: str = "default sequence description"
    ) -> None:
        """Initialize sequence narrative object."""
        super().__init__(name=name, desc=desc)
        print("init Sequence")
        self.parent: typing.Optional[Union[Show.Show, Episode.Episode]] = None
        self.children: typing.Optional[Union[List[Scene.Scene], List[Shot.Shot]]] = None
