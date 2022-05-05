"""add foreign-key to posts table


Revision ID: 13039dd8fbed
Revises: 6acac4fe8ab3
Create Date: 2022-05-04 23:31:51.142521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13039dd8fbed'
down_revision = '6acac4fe8ab3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
