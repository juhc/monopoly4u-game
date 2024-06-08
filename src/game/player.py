from .fields import AbstractField
from .schemas import PlayerResponse


class Player:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__current_field: AbstractField = None
        self.__previous_field: AbstractField = None
        self.__balance = 15000
        self.doubles = 0
        self.rounds_jail = 0
        self.in_jail = False
        self.properties: list[AbstractField] = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def current_field(self) -> AbstractField:
        return self.__current_field

    @property
    def balance(self) -> int:
        return self.__balance

    @current_field.setter
    def current_field(self, new_field: AbstractField) -> None:
        self.__previous_field = self.current_field
        self.__current_field = new_field

    @property
    def previous_field(self) -> AbstractField:
        return self.__previous_field

    def model_dump(self) -> PlayerResponse:
        current_field = self.current_field.model_dump() if self.current_field else None
        return PlayerResponse(name=self.name, balance=self.balance, current_field=current_field)
