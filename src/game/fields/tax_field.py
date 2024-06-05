from .abstract_field import AbstractField


class TaxField(AbstractField):
    def __init__(self, name: str, value: int) -> None:
        super().__init__(name)
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value