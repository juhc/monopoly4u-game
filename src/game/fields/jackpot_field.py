from field_action import FieldAction, ActionType
from .abstract_field import AbstractField
from random import randint


class JackpotField(AbstractField):
    def __init__(self) -> None:
        super().__init__("Джекпот")
        self.__cost = 1000
    
    # При входе на поле
    def on_enter(self, player_name: str) -> FieldAction:
        return FieldAction(action_type = ActionType.CHOOSE, description = f"Игрок {player_name} должен согласиться и заплатить {self.__cost} или отказаться от игры в джекпот", value = self.__cost)
    
    # При принятии
    def on_accept(self, player_name: str, dice_values: list[int]) -> FieldAction:
        dice_value = randint(1, 6)
        if dice_value in dice_values:
            value = 6000 // len(dice_values)
            return FieldAction(action_type = ActionType.EARN, description = f"Игрок {player_name} побеждает и получает {value}", value = value)
        else:
            return FieldAction(action_type = ActionType.DO_NOTHING, description = f"Игрок {player_name} проигрывает и ничего не получает")
    
    # При отказе
    def on_decline(self, player_name: str) -> FieldAction:
        return FieldAction(action_type = ActionType.DO_NOTHING, description = f"Игрок {player_name} отказывается от игры в джекпот")