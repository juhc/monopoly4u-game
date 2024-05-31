from player import Player
from fields import AbstractField, StartField
from dice import Dice


class Board:
    def __init__(self) -> None:
        self.__players: list[Player]
        self.__current_player: Player
        self.__fields: list[AbstractField]
        self.__dice = Dice()

    def add_player(self, player: Player) -> None:
        self.__players.append(Player)

    def start(self) -> None:
        self.__current_player = self.__players[0]

        for player in self.__players:
            player.current_field = self.__fields[0]

    @property
    def current_player(self) -> Player:
        return self.__current_player

    def make_move(self) -> None:
        player_field = self.current_player.current_field

        steps = self.__dice.roll()
        new_field_index = (self.__fields.index(player_field) + steps) % len(
            self.__fields
        )
        new_field = self.__fields[new_field_index]

        self.current_player.current_field = new_field
