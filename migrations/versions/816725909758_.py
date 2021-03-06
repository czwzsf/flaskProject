"""empty message

Revision ID: 816725909758
Revises: a268901c2f89
Create Date: 2022-03-30 08:04:34.454883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '816725909758'
down_revision = 'a268901c2f89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('Engine_number', table_name='mis')
    op.drop_index('chassis_number', table_name='mis')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('chassis_number', 'mis', ['chassis_number'], unique=False)
    op.create_index('Engine_number', 'mis', ['Engine_number'], unique=False)
    # ### end Alembic commands ###
