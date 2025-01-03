"""Episode class."""
import typing
from typing import List, Union

from netflix_vfx_naming import Base, Scene, Season, Sequence, Show


class Episode(Base.Base):
    """Episode narrative object."""

    def __init__(self) -> None:
        """Initialize episode narrative object."""
        super().__init__()
        print("init Episode")
        self.name = "default_episode"
        self.desc = "default episode description"
        self.parent: typing.Optional[Union[Season.Season, Show.Show]] = None
        self.children: typing.Optional[
            Union[List[Scene.Scene], List[Sequence.Sequence]]
        ] = None
