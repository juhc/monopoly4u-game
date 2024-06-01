from .abstract_group import AbstractGroup


class SpecialGroup(AbstractGroup):
    def __init__(self, name: str, color: str, field_cost: int, operation: str) -> None:
        super().__init__(name, color, field_cost)
        self.__operation = operation
    
    @property
    def operation(self) -> str:
        return self.__operation