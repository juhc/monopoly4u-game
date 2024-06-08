from ..field_action import FieldAction, ActionType
from .abstract_field import AbstractField

import sys
from pathlib import Path

sys.path.append(Path(__file__).parent)

class StartField(AbstractField):
    def __init__(self) -> None:
        super().__init__("Старт")
        self.__bonus = 1000
    
    # При входе на поле
    def on_enter(self, player_name: str) -> FieldAction:
        return FieldAction(action_type = ActionType.EARN, description = f"Игрок {player_name} получает {self.__bonus} в виде бонуса за попадания на поле {self.name}", value = self.__bonus)