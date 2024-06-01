from .abstract_field import AbstractField


class JailField(AbstractField):
    def __init__(self) -> None:
        self.__name = "Тюрьма / Посещение"
        super().__init__(self.__name)