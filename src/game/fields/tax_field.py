from field_action import FieldAction, ActionType
from .abstract_field import AbstractField


class TaxField(AbstractField):
    def __init__(self, name: str, value: int) -> None:
        super().__init__(name)
        self.__value = value
    
    # При входе на поле
    def on_enter(self, player_name: str) -> FieldAction:
        return FieldAction(action_type = ActionType.PAY, description = f"Игрок {player_name} должен заплатить {self.__value} за попадание на поле {self.name}", value = self.__value)