from field_action import FieldAction, ActionType
from .selling_field import SellingField
from groups import Operation


class SpecialField(SellingField):
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    # Аренда в зависимости от имеющихся у игрока полей группы
    @property
    def __current_rent(self) -> int:
        if self.owner_name is not None and not self.is_pledged:
            count = 0
            for field in self.group.fields:
                if field.owner_name == self.owner_name:
                    count += 1
            match self.group.operation:
                case Operation.SUM:
                    rent = self.group.field_cost * pow(2, count - 1) // 8
                case Operation.MULTIPLICATION:
                    rent = 100 + self.group.field_cost * (count - 1) // 10
            return rent
        return None
    
    # При входе на поле
    def on_enter(self, player_name: str, dices_sum_value: int) -> FieldAction:
        if self.owner_name == player_name:
            return FieldAction(action_type = ActionType.DO_NOTHING, description = f"Игрок {player_name} пришёл на своё поле {self.name}")
        if self.owner_name is not None and not self.is_pledged:
            rent = self.__current_rent if self.group.operation == Operation.SUM else dices_sum_value * self.__current_rent
            return FieldAction(action_type = ActionType.PAY, description = f"Игрок {player_name} должен заплатить {rent} за арендную плату поля {self.name} игроку {self.owner_name}", value = rent, to_player_name = self.owner_name)
        if self.is_pledged:
            return FieldAction(action_type = ActionType.DO_NOTHING, description = f"Игрок {player_name} пришёл на поле {self.name}, находящееся под залогом")
        return FieldAction(action_type = ActionType.PAY, description = f"Игрок {player_name} должен заплатить {self.group.field_cost} за покупку поля {self.name}", value = self.group.field_cost)
    
    # Покупка поля
    def buy(self, player_name: str) -> bool:
        return super().buy(player_name)
    
    # Сброс свойств поля
    def reset(self) -> None:
        super().reset()
    
    # При залоге поля
    def on_pledge(self, player_name: str) -> FieldAction:
        return super().on_pledge(player_name)
    
    # Залог поля
    def pledge(self, player_name: str) -> bool:
        return super().pledge(player_name)
    
    # При выкупе поля
    def on_ransom(self, player_name: str) -> FieldAction:
        return super().on_ransom(player_name)
    
    # Выкуп поля
    def ransom(self, player_name: str) -> bool:
        return super().ransom(player_name)