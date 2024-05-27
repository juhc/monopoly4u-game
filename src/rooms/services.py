from sqlalchemy import select, insert, update, delete, Result
from sqlalchemy.orm import selectinload

from database.models import Rooms
from database import db_helper


class RoomService:
    def __init__(self, session) -> None:
        self.__session = session

    async def create(self, **values):
        query = insert(Rooms).values(**values).returning(Rooms)
        result: Result = await self.__session.execute(query)
        await self.__session.commit()
        return result.scalar_one()

    async def select_all(self):
        query = select(Rooms).options(selectinload(Rooms.players_states))
        result: Result = await self.__session.execute(query)
        return result.scalars().all()

    async def select_one(self, **filter_by):
        query = select(Rooms).options(selectinload(Rooms.players_states)).filter_by(**filter_by)
        result: Result = await self.__session.execute(query)
        return result.scalar_one()
    
    async def delete_one(self, **filter_by):
        query = delete(Rooms).filter_by(**filter_by).returning(Rooms)
        result: Result = await self.__session.execute(query)
        await self.__session.commit()
        return result.scalar_one_or_none()