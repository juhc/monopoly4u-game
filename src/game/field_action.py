from enum import Enum


class ActionType(Enum):
    PAY = 0
    EARN = 1
    MOVE = 2
    GO_TO_JAIL = 3
    DO_NOTHING = 4
    CHOOSE = 5
    ERROR = 6

class FieldAction:
    def __init__(self, action_type: ActionType, description: str, value: int = None, to_player_name: str = None) -> None:
        self.__action_type = action_type
        self.__description = description
        self.__value = value
        self.__to_player_name = to_player_name
    
    @property
    def action_type(self) -> ActionType:
        return self.__action_type
    
    @property
    def description(self) -> str:
        return self.__description
    
    @property
    def value(self) -> int:
        return self.__value
    
    @property
    def to_player_name(self) -> str:
        return self.__to_player_name