"""Season class."""
import typing
from typing import List

from netflix_vfx_naming import Base, Episode, Show


class Season(Base.Base):
    """Season narrative object."""

    def __init__(self) -> None:
        """Initialize season narrative object."""
        super().__init__()
        print("init Season")
        self.name = "default_season"
        self.desc = "default season description"
        self.parent: typing.Optional[Show.Show] = None
        self.children: typing.Optional[List[Episode.Episode]] = None
