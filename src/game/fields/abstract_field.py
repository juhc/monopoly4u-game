from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from field_action import FieldAction


class AbstractField(ABC):
    def __init__(self, name: str) -> None:
        self.__name = name
    
    # Название поля
    @property
    def name(self) -> str:
        return self.__name
    
    # При входе на поле
    @abstractmethod
    def on_enter(self, player_name: str) -> "FieldAction":
        pass