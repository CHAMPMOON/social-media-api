"""create posts table

Revision ID: 0b363ff365e8
Revises:
Create Date: 2022-02-06 13:32:29.621391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b363ff365e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False)
    )


def downgrade():
    op.drop_table("posts")
