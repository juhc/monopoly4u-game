from fields import AbstractField, StartField


class Player:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__current_field: AbstractField
        self.__previous_field: AbstractField
        self.__balance = 15000
        self.doubles = 0
        self.rounds_jail = 0
        self.in_jail = False
        self.propperties: list[AbstractField] = []

    @property
    def current_field(self) -> AbstractField:
        return self.current_field

    @current_field.setter
    def current_field(self, new_field: AbstractField) -> None:
        self.__previous_field = self.current_field
        self.__current_field = new_field
