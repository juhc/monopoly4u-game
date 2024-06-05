from .abstract_field import AbstractField
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from groups import AbstractGroup


class SellingField(AbstractField):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__group: "AbstractGroup"
    
    # Группа
    @property
    def group(self) -> "AbstractGroup":
        return self.__group
    
    @group.setter
    def group(self, value: "AbstractGroup") -> None:
        self.__group = value