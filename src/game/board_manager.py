from .board import Board


class BoardManager:
    def __init__(self) -> None:
        self.__boards: dict[int, Board] = dict()

    def add_board(self, room_id: str, board: Board) -> None:
        self.__boards[room_id] = board

    @property
    def boards(self) -> dict[int, Board]:
        return self.__boards