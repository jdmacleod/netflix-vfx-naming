"""Show class."""
import typing
from typing import List, Union

from netflix_vfx_naming import Base, Episode, Scene, Season, Sequence


class Show(Base.Base):
    """Show narrative object."""

    def __init__(self) -> None:
        """Initialize show narrative object."""
        super().__init__()
        print("init Show")
        self.name = "default_show"
        self.desc = "default show description"
        self.children: typing.Optional[
            Union[
                List[Episode.Episode],
                List[Season.Season],
                List[Scene.Scene],
                List[Sequence.Sequence],
            ]
        ] = None
