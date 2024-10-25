"""add status parameter to booking model

Revision ID: b42aecd2a369
Revises: 2b53e7e3cb8d
Create Date: 2024-10-25 01:42:43.108804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b42aecd2a369'
down_revision: Union[str, None] = '2b53e7e3cb8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Bookings', sa.Column('status', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Bookings', 'status')
    # ### end Alembic commands ###
