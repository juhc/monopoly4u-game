from .abstract_field import AbstractField


class JackpotField(AbstractField):
    def __init__(self) -> None:
        self.__name = "Джекпот"
        super().__init__(self.__name)