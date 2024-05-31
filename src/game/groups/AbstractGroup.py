from abc import ABC

class AbstractGroup(ABC):
    def __init__(self, name: str, color: str, fields: list[int]) -> None:
        self.__name = name
        self.__color = color
        self.__fields = fields

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def color(self) -> str:
        return self.__color
    
    @property
    def fields(self) -> list[int]:
        return self.__fields