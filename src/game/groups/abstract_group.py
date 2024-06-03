from abc import ABC
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from fields import SellingField


class AbstractGroup(ABC):
    def __init__(self, name: str, color: str, field_cost: int) -> None:
        self.__name = name
        self.__color = color
        self.__field_cost = field_cost
        self.__field_pledge = int(field_cost * 0.5)
        self.__field_ransom = int(field_cost * 0.6)
        self.__fields: list["SellingField"] = []
    
    # Название группы
    @property
    def name(self) -> str:
        return self.__name
    
    # HEX-код цвета группы
    @property
    def color(self) -> str:
        return self.__color
    
    # Стоимость поля группы
    @property
    def field_cost(self) -> int:
        return self.__field_cost
    
    # Залог поля группы
    @property
    def field_pledge(self) -> int:
        return self.__field_pledge
    
    # Выкуп поля группы
    @property
    def field_ransom(self) -> int:
        return self.__field_ransom
    
    # Список полей группы
    @property
    def fields(self) -> list["SellingField"]:
        return self.__fields