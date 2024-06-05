from .abstract_group import AbstractGroup
from enum import Enum


class Operation(Enum):
    SUM = 0
    MULTIPLICATION = 1

class SpecialGroup(AbstractGroup):
    def __init__(self, name: str, color: str, field_cost: int, operation: int) -> None:
        super().__init__(name, color, field_cost)
        self.__operation = Operation(operation)
        self.__one_field_field_rent = field_cost // 8 if operation == 0 else 100
        self.__two_fields_field_rent = field_cost // 4 if operation == 0 else 100 + field_cost // 10
        self.__three_fields_field_rent = field_cost // 2 if operation == 0 else None
        self.__four_fields_field_rent = field_cost if operation == 0 else None
    
    # Операция группы
    @property
    def operation(self) -> Operation:
        return self.__operation
    
    # Аренда поля группы при наличии одного поля
    @property
    def one_field_field_rent(self) -> int:
        return self.__one_field_field_rent
    
    # Аренда поля группы при наличии двух полей
    @property
    def two_fields_field_rent(self) -> int:
        return self.__two_fields_field_rent
    
    # Аренда поля группы при наличии трёх полей
    @property
    def three_fields_field_rent(self) -> int | None:
        return self.__three_fields_field_rent
    
    # Аренда поля группы при наличии четырёх полей
    @property
    def four_fields_field_rent(self) -> int | None:
        return self.__four_fields_field_rent