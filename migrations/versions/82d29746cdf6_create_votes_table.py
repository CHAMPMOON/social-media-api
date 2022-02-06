"""create votes table

Revision ID: 82d29746cdf6
Revises: 88addbe4a816
Create Date: 2022-02-06 14:44:48.994155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82d29746cdf6'
down_revision = '88addbe4a816'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "votes",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("post_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["post_id"], ["posts.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id", "post_id")
    )


def downgrade():
    op.drop_table("votes")
