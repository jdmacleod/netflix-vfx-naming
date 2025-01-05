"""Season class."""

import typing
from typing import List

from netflix_vfx_naming import Base, Episode, Show, logger


class Season(Base.Base):
    """Season narrative object."""

    def __init__(
        self, name: str = "default_season", desc: str = "default season description"
    ) -> None:
        """Initialize season narrative object."""
        super().__init__(name=name, desc=desc)
        logger.debug("init Season")
        self.parent: typing.Optional[Show.Show] = None
        self.children: typing.Optional[List[Episode.Episode]] = None
