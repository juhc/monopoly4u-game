from ..field_action import FieldAction, ActionType
from .abstract_field import AbstractField

import sys
from pathlib import Path

sys.path.append(Path(__file__).parent)


class GoToJailField(AbstractField):
    def __init__(self) -> None:
        super().__init__("Отправляйтесь в тюрьму")

    # При входе на поле
    def on_enter(self, player_name: str) -> FieldAction:
        return FieldAction(
            action_type=ActionType.GO_TO_JAIL,
            description=f"Игрок {player_name} отправляется в тюрьму",
        )
