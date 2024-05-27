from fastapi import APIRouter, Depends, Request

import json

from .services import RoomService
from .schemas import (
    RoomResponse,
    UserRoomCreatedResponse,
    UserRoomAddToRoomResponse,
    UserRoomResponse,
)

from database import db_helper

from rooms_users.services import RoomsUsersService


router = APIRouter(prefix="/rooms", tags=["Rooms"])


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
