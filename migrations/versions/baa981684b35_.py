"""empty message

Revision ID: baa981684b35
Revises: 1912220d6b7e
Create Date: 2019-03-31 16:41:00.351590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baa981684b35'
down_revision = '1912220d6b7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.add_column(sa.Column('height', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('width', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.drop_column('width')
        batch_op.drop_column('height')

    # ### end Alembic commands ###
