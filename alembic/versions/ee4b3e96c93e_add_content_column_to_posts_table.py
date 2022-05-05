"""add content column to posts table


Revision ID: ee4b3e96c93e
Revises: 4b6a00fd6e8c
Create Date: 2022-05-04 23:10:56.355015

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ee4b3e96c93e'
down_revision = '4b6a00fd6e8c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('content', sa.String, nullable=False))


def downgrade():
    op.drop_column("posts", "content")
