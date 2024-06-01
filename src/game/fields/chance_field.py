from .abstract_field import AbstractField


class ChanceField(AbstractField):
    def __init__(self) -> None:
        self.__name = "Шанс"
        super().__init__(self.__name)