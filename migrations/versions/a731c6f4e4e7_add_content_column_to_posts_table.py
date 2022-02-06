"""add content column to posts table

Revision ID: a731c6f4e4e7
Revises: 0b363ff365e8
Create Date: 2022-02-06 13:50:14.420228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a731c6f4e4e7'
down_revision = '0b363ff365e8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("content", sa.String(), nullable=False)
    )


def downgrade():
    op.drop_column("posts", "content")
