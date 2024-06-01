from .abstract_field import AbstractField
from groups import AbstractGroup

class SellingField(AbstractField):
    def __init__(self, name: str, group: AbstractGroup) -> None:
        super().__init__(name)
        self.__group = group
    
    @property
    def group(self) -> AbstractGroup:
        return self.__group
    
    @group.setter
    def group(self, value: AbstractGroup) -> None:
        self.__group = value