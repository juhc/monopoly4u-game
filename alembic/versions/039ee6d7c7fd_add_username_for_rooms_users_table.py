"""Add: username for rooms_users table

Revision ID: 039ee6d7c7fd
Revises: 60f1c092a0e0
Create Date: 2024-05-27 00:40:15.074295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '039ee6d7c7fd'
down_revision: Union[str, None] = '60f1c092a0e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
