from fastapi import APIRouter, Depends, Request

from .services import RoomService
from .schemas import (
    RoomResponse,
    UserRoomCreatedResponse,
    UserRoomAddToRoomResponse,
    UserRoomResponse,
    MakeMoveResponse,
)

from game.board import Board
from game.player import Player
from game.board_manager import BoardManager
from game.fields import SpecialField

from database import db_helper

from rooms_users.services import RoomsUsersService


router = APIRouter(prefix="/rooms", tags=["Rooms"])

board_manager = BoardManager()


@router.post("/")
async def add_room(
    request: Request,
    session=Depends(db_helper.session_dependency),
) -> UserRoomCreatedResponse:
    data = await request.json()
    user_id = data["user_id"]
    username = data["username"]
    players_total = data["players_count"]

    created_room = await RoomService(session=session).create(
        players_total=players_total
    )
    created_player_state_db = await RoomsUsersService(session=session).create(
        room_id=created_room.id, user_id=user_id, username=username
    )
    created_player_state = UserRoomResponse.model_validate(created_player_state_db)
    return UserRoomCreatedResponse(
        **created_player_state.model_dump(),
        players_total=created_room.players_total,
        room_id=created_player_state_db.room_id
    )


@router.get("/{room_id}")
async def get_room(
    room_id: int,
    session=Depends(db_helper.session_dependency),
) -> RoomResponse:
    room = await RoomService(session=session).select_one(id=room_id)
    response = RoomResponse(
        room_id=room.id, players_total=room.players_total, users=room.players_states
    )
    return response


@router.delete("/{room_id}")
async def get_room(
    room_id: int,
    session=Depends(db_helper.session_dependency),
) -> RoomResponse:
    room_deleted = await RoomService(session=session).delete_one(id=room_id)
    response = RoomResponse(
        room_id=room_deleted.id, players_total=room_deleted.players_total
    )
    return response


@router.get("/")
async def get_rooms(
    session=Depends(db_helper.session_dependency),
) -> list[RoomResponse]:
    rooms = await RoomService(session=session).select_all()
    response = [
        RoomResponse(
            room_id=room.id, players_total=room.players_total, users=room.players_states
        )
        for room in rooms
    ]
    return response


@router.post("/{room_id}")
async def add_player_to_room(
    room_id: int, request: Request, session=Depends(db_helper.session_dependency)
) -> UserRoomAddToRoomResponse:
    data = await request.json()
    user_id = data["user_id"]
    username = data["username"]
    added_player = await RoomsUsersService(session=session).create(
        room_id=room_id, user_id=user_id, username=username
    )
    return added_player


@router.delete("/players/{user_id}")
async def delete_player_state(
    user_id: str, session=Depends(db_helper.session_dependency)
) -> UserRoomAddToRoomResponse | None:
    deleted_player = await RoomsUsersService(session=session).delete_one(
        user_id=user_id
    )

    return deleted_player


@router.post("/{room_id}/game")
async def init_game(room_id: int):
    if room_id not in board_manager.boards.keys():
        game = Board()
        board_manager.add_board(room_id=room_id, board=game)

    return board_manager.boards[room_id].model_dump()


@router.get("/{room_id}/game")
async def get_game(room_id: int):
    if room_id in board_manager.boards.keys():
        game = board_manager.boards[room_id]

        return game.model_dump()


@router.patch("/{room_id}/game")
async def add_player_in_game(room_id: int, request: Request):
    data = await request.json()
    username = data.get("username")
    board_manager.boards[room_id].add_player(Player(username))

    return board_manager.boards[room_id].model_dump()


@router.post("/{room_id}/game/start")
async def start_game(room_id: int):
    board_manager.boards[room_id].start()
    return board_manager.boards[room_id].model_dump()


@router.post("/{room_id}/game/roll-dice")
async def roll_dice(room_id: int, requst: Request):
    data = await requst.json()
    username = data.get("username")

    game = board_manager.boards[room_id]
    player = game.get_player_by_name(username)

    if player and player is game.current_player:
        game.roll_dice()

        return game.dice.model_dump()


@router.post("/{room_id}/game/make-move")
async def make_move(room_id: int, requst: Request):
    data = await requst.json()
    username = data.get("username")

    game = board_manager.boards[room_id]
    player = game.get_player_by_name(username)

    if player and player is game.current_player:
        field = game.make_move()
        if type(field) is SpecialField:
            description = field.on_enter(username, game.dice.score).description
        else:
            description = field.on_enter(username).description

        game.next_player()

        response = MakeMoveResponse(
            description=description, **game.model_dump().model_dump()
        )
        return response
