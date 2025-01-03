"""Shot class."""
import typing
from typing import List, Union

from netflix_vfx_naming import Base, Scene, Sequence


class Shot(Base.Base):
    """Shot narrative object."""

    def __init__(self) -> None:
        """Initialize shot narrative object."""
        super().__init__()
        print("init Shot.")
        self.name = "default_shot"
        self.desc = "default shot description"
        self.parent: typing.Optional[Union[Scene.Scene, Sequence.Sequence]] = None

    def get_fullname(self) -> str:
        """Get full name of Shot, traversing hierarchy."""
        node_parent: typing.Any = self.parent
        fullname = self.name
        while node_parent:
            name_part = node_parent.name
            fullname = "_".join([name_part, fullname])
            node_parent = node_parent.parent

        return fullname
