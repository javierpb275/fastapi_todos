"""create address_id to users

Revision ID: bf35fea9ec67
Revises: 8648a4be0ab5
Create Date: 2023-06-17 16:31:42.003093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf35fea9ec67'
down_revision = '8648a4be0ab5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table="users", referent_table="address", local_cols=["address_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("address_users_fk", table_name="users")
    op.drop_column('users', 'address_id')
