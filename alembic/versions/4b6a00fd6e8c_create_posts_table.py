"""create posts table

Revision ID: 4b6a00fd6e8c
Revises: 
Create Date: 2022-05-04 22:59:30.075635

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '4b6a00fd6e8c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer, nullable=False, primary_key=True),
                    sa.Column('title', sa.String, nullable=False))


def downgrade():
    op.drop_table('posts')
