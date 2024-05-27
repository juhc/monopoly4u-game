from pydantic import BaseModel


class UserRoomResponse(BaseModel):
    user_id: str
    balance: int
    current_cell: int | None
    username: str

    class Config:
        from_attributes = True

class UserRoomAddToRoomResponse(UserRoomResponse):
    room_id: int

    class Config:
        from_attributes = True

class UserRoomCreatedResponse(UserRoomResponse):
    room_id: int
    players_total: int

    class Config:
        from_attributes = True


class RoomResponse(BaseModel):
    room_id: int
    players_total: int
    users: list[UserRoomResponse | None] = []

    class Config:
        from_attributes = True
