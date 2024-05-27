from typing import TYPE_CHECKING
import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import text

from .base import Base

if TYPE_CHECKING:
    from .rooms_users import RoomsUsers


class Rooms(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    players_total: Mapped[int] = mapped_column(
        default=2, server_default=text("2"), nullable=False
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    players_states: Mapped[list["RoomsUsers"]] = relationship(back_populates="room")
