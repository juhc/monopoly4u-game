from .abstract_group import AbstractGroup

class CommonGroup(AbstractGroup):
    def __init__(self, name: str, color: str, field_cost: int) -> None:
        super().__init__(name, color, field_cost)
    