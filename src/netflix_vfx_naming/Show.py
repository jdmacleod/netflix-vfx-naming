"""Show class."""

import typing
from typing import List, Union

from netflix_vfx_naming import Base, Episode, Scene, Season, Sequence, logger


class Show(Base.Base):
    """Show narrative object."""

    def __init__(
        self, name: str = "default_show", desc: str = "default show description"
    ) -> None:
        """Initialize show narrative object."""
        super().__init__(name=name, desc=desc)
        logger.debug("init Show")
        self.children: typing.Optional[
            Union[
                List[Episode.Episode],
                List[Season.Season],
                List[Scene.Scene],
                List[Sequence.Sequence],
            ]
        ] = None
