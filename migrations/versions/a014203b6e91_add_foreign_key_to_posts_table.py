"""add foreign key to posts table

Revision ID: a014203b6e91
Revises: b85c0aeec2c8
Create Date: 2022-02-06 14:20:11.543833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a014203b6e91'
down_revision = 'b85c0aeec2c8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("owner_id", sa.Integer(), nullable=False)
    )
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE"
    )


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
