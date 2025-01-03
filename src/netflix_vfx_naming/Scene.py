"""Scene class."""
import typing
from typing import List, Union

from netflix_vfx_naming import Base, Episode, Sequence, Shot, Show


class Scene(Base.Base):
    """Scene narrative object."""

    def __init__(self) -> None:
        """Initialize scene narrative object."""
        super().__init__()
        print("init Scene")
        self.name = "default_scene"
        self.desc = "default scene description"
        self.parent: typing.Optional[
            Union[Sequence.Sequence, Episode.Episode, Show.Show]
        ] = None
        self.children: typing.Optional[List[Shot.Shot]] = None
