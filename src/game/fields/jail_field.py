from field_action import FieldAction, ActionType
from .abstract_field import AbstractField


class JailField(AbstractField):
    def __init__(self) -> None:
        super().__init__("Тюрьма / Посещение")
        self.__prisoners: list[str] = []
        self.__getting_out_cost = 500
    
    # Список заключённых
    @property
    def prisoners(self) -> list[str]:
        return self.__prisoners
    
    # При входе на поле
    def on_enter(self, player_name: str) -> FieldAction:
        return FieldAction(action_type = ActionType.DO_NOTHING, description = f"Игрок {player_name} посещает тюрьму")
    
    # При оплате за выход
    def on_pay_to_leave(self, player_name: str) -> FieldAction:
        if player_name in self.__prisoners:
            return FieldAction(action_type = ActionType.PAY, description = f"Игрок {player_name} должен заплатить {self.__getting_out_cost} за выход из тюрьмы", value = self.__getting_out_cost)
        return FieldAction(action_type = ActionType.ERROR, description = f"Игрок {player_name} не является заключённым")
    
    # При выпадении дубля
    def on_double(self, player_name: str) -> FieldAction:
        if player_name in self.__prisoners:
            return FieldAction(action_type = ActionType.DO_NOTHING, description = f"Игрок {player_name} выбросил дубль и вышел из тюрьмы из тюрьмы")
        return FieldAction(action_type = ActionType.ERROR, description = f"Игрок {player_name} не является заключённым")
    
    # Выход из тюрьмы
    def leave(self, player_name: str) -> bool:
        if player_name in self.__prisoners:
            self.__prisoners.remove(player_name)
            return True
        return False