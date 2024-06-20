from ..field_action import FieldAction, ActionType
from .abstract_field import AbstractField
from random import randint

import sys
from pathlib import Path

sys.path.append(Path(__file__).parent)

class ChanceField(AbstractField):
    def __init__(self) -> None:
        super().__init__("Шанс")
    
    # При входе на поле
    def on_enter(self, player_name: str) -> FieldAction:
        action_type = ActionType(randint(0, 3))
        match action_type:
            case ActionType.PAY:
                services = ["услуги стоматолога", "ремонт автомобиля", "покупки в магазине одежды", "счёт в ресторане"]
                values = [250, 500, 750, 1000]
                value = values[randint(0, len(values) - 1)]
                description = f"Игрок {player_name} должен залатить {value} за {services[randint(0, len(services) - 1)]}"
            case ActionType.EARN:
                awards = ["выигрыша в казино", "приза за победу в конкурсе красоты", "премиального вознаграждения", "подарка на день рождения"]
                values = [250, 500, 750, 1000]
                value = values[randint(0, len(values) - 1)]
                description = f"Игрок {player_name} получает {value} в качестве {awards[randint(0, len(awards) - 1)]}"
            case ActionType.MOVE:
                direction = randint(0, 1)
                value = pow(-1, direction) * randint(2, 12)
                description = f"Игрок {player_name} переходит на {abs(value)} {'поля' if abs(value) < 5 else 'полей'} {'вперёд' if direction == 0 else 'назад'}"
            case ActionType.GO_TO_JAIL:
                value = None
                description = f"Игрок {player_name} отправляется в тюрьму"
        return FieldAction(action_type = action_type, description = description, value = value)