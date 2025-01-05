"""Base narrative object."""

import typing
from typing import List

from netflix_vfx_naming import logger


class Base:
    """Base narrative object."""

    def __init__(
        self, name: str = "base_object", desc: str = "base description"
    ) -> None:
        """Initialize base narrative object."""
        logger.debug("init Base.")
        self.id: typing.Optional[int] = None
        self.name: str = name
        self.desc: str = desc

        self.parent: typing.Optional[typing.Any] = None
        self.children: typing.Optional[List[typing.Any]] = None

    def add_child(self, child: typing.Any, set_parent: bool = True) -> bool:
        """Add a child object.

        Args:
            child (typing.Any): the child object to add.
            set_parent (bool): if True, set the parent on the child object.

        Returns:
            bool: return True if the child was added, False otherwise.
        """
        if isinstance(self.children, list):
            try:
                self.children.append(child)
                if set_parent:
                    try:
                        child.set_parent(self, add_child=False)
                    except BaseException as e:
                        logger.error(
                            f"could not set parent for child {child} to object {self}: {e}"
                        )
                return True
            except BaseException as e:
                logger.error(f"could not append child {child} to object {self}: {e}")
                return False
        else:
            try:
                self.children = [child]
                if set_parent:
                    try:
                        child.set_parent(self, add_child=False)
                    except BaseException as e:
                        logger.error(
                            f"could not set parent for child {child} to object {self}: {e}"
                        )
                return True
            except BaseException as e:
                logger.error(f"could not add child {child} to object {self}: {e}")
                return False

    def remove_child(self, child: typing.Any, set_parent: bool = True) -> bool:
        """Remove a child object.

        Args:
            child (typing.Any): the child object to remove.
            set_parent (bool): if True, set parent on the child object to None.

        Returns:
            bool: return True if the child was removed, False otherwise.
        """
        if isinstance(self.children, list):
            try:
                self.children.remove(child)
                if set_parent:
                    try:
                        child.set_parent(None, add_child=False)
                    except BaseException as e:
                        logger.error(
                            f"could not set parent for child {child} to None: {e}"
                        )
                return True
            except BaseException as e:
                logger.error(f"could not remove child {child} from object {self}: {e}")
                return False
        else:
            return False

    def set_parent(self, parent: typing.Any, add_child: bool = True) -> bool:
        """Set the parent object.

        Args:
            parent (typing.Any): the parent object to set.
            add_child (bool): if True, add the child to the parent's children.

        Returns:
            bool: return True if the parent was set, False otherwise.
        """
        if self.parent:
            self.parent.remove_child(self, set_parent=False)
        try:
            self.parent = parent
            if add_child:
                try:
                    parent.add_child(self, set_parent=False)
                except BaseException as e:
                    logger.error(
                        f"could not add child {self} to parent object {parent}: {e}"
                    )
            return True
        except BaseException as e:
            logger.error(f"could not set parent {parent} for object {self}: {e}")
            return False
