"""Episode class."""

import typing
from typing import List, Union

from netflix_vfx_naming import Base, Scene, Season, Sequence, Show, logger


class Episode(Base.Base):
    """Episode narrative object."""

    def __init__(
        self, name: str = "default_episode", desc: str = "default episode description"
    ) -> None:
        """Initialize episode narrative object."""
        super().__init__(name=name, desc=desc)
        logger.debug("init Episode")
        self.parent: typing.Optional[Union[Season.Season, Show.Show]] = None
        self.children: typing.Optional[
            Union[List[Scene.Scene], List[Sequence.Sequence]]
        ] = None
