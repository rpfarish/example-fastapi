"""add user table


Revision ID: 6acac4fe8ab3
Revises: ee4b3e96c93e
Create Date: 2022-05-04 23:17:42.892910

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6acac4fe8ab3'
down_revision = 'ee4b3e96c93e'
branch_labels = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('email', sa.String, nullable=False),
                    sa.Column('password', sa.String, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


depends_on = None


def downgrade():
    op.drop_table('users')
