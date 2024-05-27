"""empty message

Revision ID: 60f1c092a0e0
Revises: 35ac347bcfcc, 86aa2b537449, a527ab7d0ece, eb48a6ad3a24
Create Date: 2024-05-27 00:39:56.697749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60f1c092a0e0'
down_revision: Union[str, None] = ('35ac347bcfcc', '86aa2b537449', 'a527ab7d0ece', 'eb48a6ad3a24')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
