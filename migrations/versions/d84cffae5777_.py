"""empty message

Revision ID: d84cffae5777
Revises: 51a5f39b3cad
Create Date: 2019-04-13 18:46:02.109570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd84cffae5777'
down_revision = '51a5f39b3cad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('issue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('store_url', sa.Unicode(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('issue', schema=None) as batch_op:
        batch_op.drop_column('store_url')

    # ### end Alembic commands ###
