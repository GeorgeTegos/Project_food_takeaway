"""empty message

Revision ID: 9c216da4dd5e
Revises: 2154974d4250
Create Date: 2023-07-28 13:18:55.721011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c216da4dd5e'
down_revision = '2154974d4250'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('order_delivered')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_delivered', sa.BOOLEAN(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
