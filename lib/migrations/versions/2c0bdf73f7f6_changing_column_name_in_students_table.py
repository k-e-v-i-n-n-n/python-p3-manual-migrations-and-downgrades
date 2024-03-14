"""Changing column name in Students table

Revision ID: 2c0bdf73f7f6
Revises: 099273207c0b
Create Date: 2024-03-14 15:10:46.210927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c0bdf73f7f6'
down_revision = '099273207c0b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'grade', new_column_name='stu_grade')


def downgrade() -> None:
    op.alter_column('scholars', 'stu_grade', new_column_name='grade')

