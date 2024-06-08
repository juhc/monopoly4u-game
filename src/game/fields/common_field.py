from ..field_action import FieldAction, ActionType
from .selling_field import SellingField

import sys
from pathlib import Path

sys.path.append(Path(__file__).parent)


class CommonField(SellingField):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__buildings_count = 0
        self.__monopoly_ratio = 1.75
        self.__building_basic_rent_difference = 200
        self.__buildings_max_count = 5
    
    # Дельта для вычисления арендной платы
    @property
    def __delta(self) -> int:
        return self.__basic_rent * 5 - 100

    # Базовая арендная плата
    @property
    def __basic_rent(self) -> int:
        if self.group.fields[-1] == self:
            return self.group.field_cost // 10
        else:
            return self.group.field_cost // 10 - 20
    
    # Арендная плата в зависимости от имеющихся у игрока полей группы и наличии зданий на поле
    @property
    def __current_rent(self) -> int | None:
        if self.owner_name is not None and not self.is_pledged:
            rent = self.__basic_rent
            for field in self.group.fields:
                if field.owner_name != self.owner_name:
                    return rent
            rent = int(rent * self.__monopoly_ratio)
            if self.__buildings_count == 0:
                return rent
            rent *= 5
            for i in range(1, self.__buildings_count):
                rent += int((self.__delta + self.__building_basic_rent_difference * i) * self.__monopoly_ratio)
            return rent
        return None
    
    # При входе на поле
    def on_enter(self, player_name: str) -> FieldAction:
        if self.owner_name == player_name:
            return FieldAction(action_type = ActionType.DO_NOTHING, description = f"Игрок {player_name} пришёл на своё поле {self.name}")
        if self.owner_name is not None and not self.is_pledged:
            return FieldAction(action_type = ActionType.PAY, description = f"Игрок {player_name} должен заплатить {self.__current_rent} за арендную плату поля {self.name} игроку {self.owner_name}", value = self.__current_rent, to_player_name = self.owner_name)
        if self.is_pledged:
            return FieldAction(action_type = ActionType.DO_NOTHING, description = f"Игрок {player_name} пришёл на поле {self.name}, находящееся под залогом")
        return FieldAction(action_type = ActionType.PAY, description = f"Игрок {player_name} должен заплатить {self.group.field_cost} за покупку поля {self.name}", value = self.group.field_cost)
    
    # Покупка поля
    def buy(self, player_name: str) -> bool:
        return super().buy(player_name)
    
    # Сброс свойств поля
    def reset(self) -> None:
        super().reset()
        self.__buildings_count = 0
    
    # При покупке здания на поле
    def on_buy_building(self, player_name: str) -> FieldAction:
        if self.owner_name == player_name and not self.is_pledged:
            return FieldAction(action_type = ActionType.PAY, description = f"Игрок {player_name} должен заплатить {self.group.field_building_cost} за покупку {self.__buildings_count + 1}-го здания на поле {self.name}", value = self.group.field_building_cost)
        return FieldAction(action_type = ActionType.ERROR, description = f"Игрок {player_name} не имеет возможности купить здание на поле {self.name}")
    
    # Покупка здания на поле
    def buy_building(self, player_name: str) -> bool:
        if self.owner_name == player_name and not self.is_pledged:
            for field in self.group.fields:
                if field.owner_name != self.owner_name:
                    return False
            if self.__buildings_count < self.__buildings_max_count:
                self.__buildings_count += 1
                return True
        return False
    
    # При продаже здания на поле
    def on_sell_building(self, player_name: str) -> FieldAction:
        if self.owner_name == player_name and self.__buildings_count > 0:
            return FieldAction(action_type = ActionType.EARN, description = f"Игрок {player_name} получает {self.group.field_building_cost} за продажу здания на поле {self.name}", value = self.group.field_building_cost)
        return FieldAction(action_type = ActionType.ERROR, description = f"Игрок {player_name} не имеет возможности продать здание на поле {self.name}")
    
    # Продажа здания на поле
    def sell_building(self, player_name: str) -> bool:
        if self.owner_name == player_name and self.__buildings_count > 0:
            self.__buildings_count -= 1
            return True
        return False
    
    # При залоге поля
    def on_pledge(self, player_name: str) -> FieldAction:
        return super().on_pledge(player_name)
    
    # Залог поля
    def pledge(self, player_name: str) -> bool:
        if self.__buildings_count == 0:
            return super().pledge(player_name)
        return False
    
    # При выкупе поля
    def on_ransom(self, player_name: str) -> FieldAction:
        return super().on_ransom(player_name)
    
    # Выкуп поля
    def ransom(self, player_name: str) -> bool:
        return super().ransom(player_name)