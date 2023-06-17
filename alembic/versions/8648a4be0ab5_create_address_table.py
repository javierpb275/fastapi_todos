"""create address table

Revision ID: 8648a4be0ab5
Revises: ef8b4d10e323
Create Date: 2023-06-17 15:08:16.055165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8648a4be0ab5'
down_revision = 'ef8b4d10e323'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(), nullable=False),
                    sa.Column('address2', sa.String(), nullable=False),
                    sa.Column('city', sa.String(), nullable=False),
                    sa.Column('state', sa.String(), nullable=False),
                    sa.Column('country', sa.String(), nullable=False),
                    sa.Column('postalcode', sa.String(), nullable=False),
                    )


def downgrade() -> None:
    op.drop_table('address')
