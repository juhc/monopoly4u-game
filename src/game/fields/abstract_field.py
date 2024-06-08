from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import sys
from pathlib import Path
sys.path.append(Path(__file__).parent.parent)

from ..schemas import FieldResponse

if TYPE_CHECKING:
    from field_action import FieldAction


class AbstractField(ABC):
    def __init__(self, name: str) -> None:
        self.__name = name

    # Название поля
    @property
    def name(self) -> str:
        return self.__name
    
    def model_dump(self) -> FieldResponse:
        return FieldResponse(name = self.name, field_type = self.__class__.__name__)
    
    # При входе на поле
    @abstractmethod
    def on_enter(self, player_name: str) -> "FieldAction":
        pass
