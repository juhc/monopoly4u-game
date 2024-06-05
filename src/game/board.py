from typing import TYPE_CHECKING

from .player import Player
from .dice import Dice
from .fields_builder import FieldsBuilder 
from .fields import AbstractField


class Board:
    def __init__(self) -> None:
        self.__players: list[Player] = []
        self.__current_player: Player = None
        self.__fields: FieldsBuilder = FieldsBuilder().fields
        self.__dice = Dice()

    def add_player(self, player: Player) -> None:
        self.__players.append(player)

    def start(self) -> None:
        self.__current_player = self.__players[0]

        for player in self.__players:
            player.current_field = self.__fields[0]

    @property
    def current_player(self) -> Player:
        return self.__current_player

    @property
    def current_player(self, next_player: Player) -> None:
        self.__current_player = next_player

    def make_move(self) -> AbstractField:
        current_player_field = self.current_player.current_field

        steps = self.__dice.roll()
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
    

    def model_dump(self) -> dict:
        return {
            "current_player": self.current_player,
            "fields": self.__fields.model_dump(),
            "players": [player.model_dump() for player in self.__players]
        }