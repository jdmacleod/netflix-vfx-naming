"""Base narrative object."""

import typing
from typing import List


class Base:
    """Base narrative object."""

    def __init__(self) -> None:
        """Initialize base narrative object."""
        print(f"init Base.")
        self.id: typing.Optional[int] = None
        self.name: str = "base_object"
        self.desc: str = "base description"

        self.parent: typing.Optional[typing.Any] = None
        self.children: typing.Optional[List[typing.Any]] = None
