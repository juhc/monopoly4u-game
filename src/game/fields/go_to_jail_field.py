from .abstract_field import AbstractField


class GoToJailField(AbstractField):
    def __init__(self) -> None:
        self.__name = "Отправляйтесь в тюрьму"
        super().__init__(self.__name)