from .abstract_group import AbstractGroup


class CommonGroup(AbstractGroup):
    def __init__(self, name: str, color: str, field_cost: int) -> None:
        super().__init__(name, color, field_cost)
        self.__field_building_cost = int(field_cost * 0.8)
    
    # Стоимость здания на поле группы
    @property
    def field_building_cost(self) -> int:
        return self.__field_building_cost