"""empty message

Revision ID: 7fd2c577ad43
Revises: 162a17ad0513
Create Date: 2024-05-27 00:47:59.343261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7fd2c577ad43'
down_revision: Union[str, None] = '162a17ad0513'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rooms', 'total')
    op.add_column('rooms_users', sa.Column('username', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rooms_users', 'username')
    op.add_column('rooms', sa.Column('total', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
