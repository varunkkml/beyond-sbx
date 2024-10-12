"""add content column to posts

Revision ID: 987af2c85e5a
Revises: 0445ff7e70ab
Create Date: 2024-10-12 03:51:34.546972

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '987af2c85e5a'
down_revision: Union[str, None] = '0445ff7e70ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
