"""Add JSON tags field to Conference table

Revision ID: bdf088ad04f8
Revises: 38236d1de5a2
Create Date: 2025-01-09 23:32:29.890374

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdf088ad04f8'
down_revision: Union[str, None] = '38236d1de5a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('conference', sa.Column('tags', sa.JSON(), nullable=True))


def downgrade() -> None:
    op.drop_column('conference', 'tags')
