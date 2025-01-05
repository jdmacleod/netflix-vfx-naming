"""Scene class."""

import typing
from typing import List, Union

from netflix_vfx_naming import Base, Episode, Sequence, Shot, Show, logger


class Scene(Base.Base):
    """Scene narrative object."""

    def __init__(
        self, name: str = "default_scene", desc: str = "default scene description"
    ) -> None:
        """Initialize scene narrative object."""
        super().__init__(name=name, desc=desc)
        logger.debug("init Scene")
        self.parent: typing.Optional[
            Union[Sequence.Sequence, Episode.Episode, Show.Show]
        ] = None
        self.children: typing.Optional[List[Shot.Shot]] = None
