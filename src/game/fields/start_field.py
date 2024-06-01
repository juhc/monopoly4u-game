from .abstract_field import AbstractField


class StartField(AbstractField):
    def __init__(self, lap_bonus: int, field_bonus: int) -> None:
        self.__name = "Старт"
        super().__init__(self.__name)
        self.__lap_bonus = lap_bonus
        self.__field_bonus = field_bonus

    @property
    def lap_bonus(self) -> int:
        return self.__lap_bonus
    
    @property
    def field_bonus(self) -> int:
        return self.__field_bonus