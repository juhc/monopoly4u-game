from pydantic import BaseModel


class FieldResponse(BaseModel):
    name: str
    field_type: str
    id: int | None = None

    class Config:
        from_attributes = True


class FieldsBuilderResponse(BaseModel):
    fields: list

    class Config:
        from_attributes = True


class PlayerResponse(BaseModel):
    name: str
    balance: int
    current_field: FieldResponse | None

    class Config:
        from_attributes = True


class DiceResponse(BaseModel):
    score: int
    cubes: list[int]
    is_double: bool


class BoardResponse(BaseModel):
    fields: list
    players: list[PlayerResponse] | list[None]
    current_player: PlayerResponse | None

    class Config:
        from_attributes = True
