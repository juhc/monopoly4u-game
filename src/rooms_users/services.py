from sqlalchemy import select, insert, Result, delete, update

from database import db_helper
from database.models import RoomsUsers


class RoomsUsersService:
    def __init__(self, session) -> None:
        self.__session = session

    async def create(self, **values):
        query = insert(RoomsUsers).values(**values).returning(RoomsUsers)
        result: Result = await self.__session.execute(query)
        await self.__session.commit()
        return result.scalar_one()

    async def update_one(self, filter: dict, values: dict):
        query = (
            update(RoomsUsers)
            .filter_by(**filter)
            .values(**values)
            .returning(RoomsUsers)
        )
        result: Result = await self.__session.execute(query)
        await self.__session.commit()
        return result.scalar_one()

    async def select_one(self, **filter_by):
        query = select(RoomsUsers).filter_by(**filter_by)
        result: Result = await self.__session.execute(query)
        return result.scalar_one_or_none()
    
    async def select_all(self, **filter_by):
        query = select(RoomsUsers).filter_by(**filter_by)
        result: Result = await self.__session.execute(query)
        return result.scalars().all()

    async def delete_one(self, **filter_by):
        query = delete(RoomsUsers).filter_by(**filter_by).returning(RoomsUsers)
        result: Result = await self.__session.execute(query)
        await self.__session.commit()
        return result.scalar_one_or_none()
