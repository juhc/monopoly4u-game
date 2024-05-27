"""Add: username for rooms_users table

Revision ID: 162a17ad0513
Revises: 039ee6d7c7fd
Create Date: 2024-05-27 00:43:23.266756

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '162a17ad0513'
down_revision: Union[str, None] = '039ee6d7c7fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
