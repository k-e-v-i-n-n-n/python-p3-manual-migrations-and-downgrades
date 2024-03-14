"""Renaming students to scholars

Revision ID: 099273207c0b
Revises: 791279dd0760
Create Date: 2024-03-14 15:03:07.182958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '099273207c0b'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
