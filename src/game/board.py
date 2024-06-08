from .player import Player
from .dice import Dice
from .fields_builder import FieldsBuilder
from .fields import AbstractField
from .schemas import BoardResponse


class Board:
    def __init__(self) -> None:
        self.__players: list[Player] = []
        self.__current_player: Player = None
        self.__fields: FieldsBuilder = FieldsBuilder().fields
        self.__dice = Dice()

    def add_player(self, player_add: Player) -> None:
        for player in self.__players:
            if player.name == player_add.name:
                return

        self.__players.append(player_add)

    def start(self) -> None:
        self.__current_player = self.__players[0]

        for player in self.__players:
            player.current_field = self.__fields[0]

    @property
    def current_player(self) -> Player:
        return self.__current_player

    @property
    def dice(self) -> Dice:
        return self.__dice

    @current_player.setter
    def current_player(self, next_player: Player) -> None:
        self.__current_player = next_player

    def roll_dice(self) -> int:
        return self.__dice.roll()

    def make_move(self) -> AbstractField:
        current_player_field = self.current_player.current_field

        steps = self.__dice.score
        new_field_index = (self.__fields.index(current_player_field) + steps) % len(
            self.__fields
        )
        new_field = self.__fields[new_field_index]

        self.current_player.current_field = new_field

        return self.current_player.current_field

    def next_player(self) -> Player:
        next_player_index = (self.__players.index(self.current_player) + 1) % len(
            self.__players
        )
        self.current_player = self.__players[next_player_index]

        return self.current_player

    def get_player_by_name(self, name) -> Player | None:
        for player in self.__players:
            if player.name == name:
                return player

    def model_dump(self) -> BoardResponse:
        players = [player.model_dump() for player in self.__players]
        if len(players):
            for player in players:
                if player.current_field:
                    player.current_field.id = self.__fields.index(
                        self.get_player_by_name(player.name).current_field
                    )
        current_player = (
            self.current_player.model_dump() if self.current_player else None
        )
        if current_player:
            current_player.current_field.id = (
                self.__fields.index(self.current_player.current_field)
                if self.current_player
                else None
            )
        fields = [field.model_dump() for field in self.__fields]
        for index, field in enumerate(fields):
            field.id = index

        return BoardResponse(
            fields=fields, players=players, current_player=current_player
        )
