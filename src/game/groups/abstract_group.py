from abc import ABC
#from fields import SellingField


class AbstractGroup(ABC):
    def __init__(self, name: str, color: str, field_cost: int) -> None:
        self.__name = name
        self.__color = color
        self.__field_cost = field_cost
        self.__fields = []

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def color(self) -> str:
        return self.__color
    
    @property
    def field_cost(self) -> int:
        return self.__field_cost
    
    @property
    def fields(self) -> list:
        return self.__fields