from .abstract_group import AbstractGroup
from enum import Enum


class Operation(Enum):
    SUM = 0
    MULTIPLICATION = 1

class SpecialGroup(AbstractGroup):
    def __init__(self, name: str, color: str, field_cost: int, operation: int) -> None:
        super().__init__(name, color, field_cost)
        self.__operation = Operation(operation)
    
    # Операция группы
    @property
    def operation(self) -> Operation:
        return self.__operation