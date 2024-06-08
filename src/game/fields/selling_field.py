from .abstract_field import AbstractField, abstractmethod
from typing import TYPE_CHECKING
from ..field_action import FieldAction, ActionType
if TYPE_CHECKING:
    from groups import AbstractGroup

import sys
from pathlib import Path

sys.path.append(Path(__file__).parent)


class SellingField(AbstractField):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__group: "AbstractGroup" = None
        self.__owner_name: str = None
        self.__is_pledged = False
    
    # Группа поля (геттер)
    @property
    def group(self) -> "AbstractGroup":
        return self.__group
    
    # Группа поля (сеттер)
    @group.setter
    def group(self, value: "AbstractGroup") -> None:
        self.__group = value

    # Имя владельца
    @property
    def owner_name(self) -> str:
        return self.__owner_name
    
    # Находится ли поле под залогом
    @property
    def is_pledged(self) -> bool:
        return self.__is_pledged
    
    # Покупка поля
    @abstractmethod
    def buy(self, player_name: str) -> bool:
        if self.__owner_name is None:
            self.__owner_name = player_name
            return True
        return False
    
    # Сброс свойств поля
    @abstractmethod
    def reset(self) -> None:
        self.__owner_name = None
        self.__is_pledged = False
    
    # При залоге поля
    @abstractmethod
    def on_pledge(self, player_name: str) -> FieldAction:
        if self.__owner_name == player_name and not self.__is_pledged:
            return FieldAction(action_type = ActionType.EARN, description = f"Игрок {player_name} получает {self.group.field_pledge} за залог поля {self.name}", value = self.group.field_pledge)
        return FieldAction(action_type = ActionType.ERROR, description = f"Игрок {player_name} не имеет возможности заложить поле {self.name}")
    
    # Залог поля
    @abstractmethod
    def pledge(self, player_name: str) -> bool:
        if self.__owner_name == player_name and not self.__is_pledged:
            self.__is_pledged = True
            return True
        return False
    
    # При выкупе поля
    @abstractmethod
    def on_ransom(self, player_name: str) -> FieldAction:
        if self.__owner_name == player_name and self.__is_pledged:
            return FieldAction(action_type = ActionType.PAY, description = f"Игрок {player_name} должен заплатить {self.group.field_ransom} за выкуп поля {self.name}", value = self.group.field_ransom)
        return FieldAction(action_type = ActionType.ERROR, description = f"Игрок {player_name} не имеет возможности выкупить поле {self.name}")
    
    # Выкуп поля
    @abstractmethod
    def ransom(self, player_name: str) -> bool:
        if self.__owner_name == player_name and self.__is_pledged:
            self.__is_pledged = False
            return True
        return False