"""Base narrative object."""

import typing
from typing import List


class Base:
    """Base narrative object."""

    def __init__(
        self, name: str = "base_object", desc: str = "base description"
    ) -> None:
        """Initialize base narrative object."""
        print(f"init Base.")
        self.id: typing.Optional[int] = None
        self.name: str = name
        self.desc: str = desc

        self.parent: typing.Optional[typing.Any] = None
        self.children: typing.Optional[List[typing.Any]] = None
