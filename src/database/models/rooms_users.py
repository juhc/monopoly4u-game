from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, CheckConstraint, text

from .base import Base

if TYPE_CHECKING:
    from .rooms import Rooms


class RoomsUsers(Base):
    __tablename__ = "rooms_users"
    __table_args__ = (CheckConstraint("balance >= 0", "check_user_room_balance"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(unique=True, nullable=False)
    room_id: Mapped[int] = mapped_column(
        ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False
    )
    balance: Mapped[int] = mapped_column(default=0, server_default=text("0"), nullable=False)
    current_cell: Mapped[int] = mapped_column(nullable=True)
    username: Mapped[str]
    room: Mapped['Rooms'] = relationship(back_populates="players_states")
