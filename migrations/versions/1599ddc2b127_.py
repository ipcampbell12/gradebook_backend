"""empty message

Revision ID: 1599ddc2b127
Revises: e1744d53c555
Create Date: 2023-02-08 14:16:37.089974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1599ddc2b127'
down_revision = 'e1744d53c555'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('teachers', schema=None) as batch_op:
        batch_op.drop_column('password')
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('teachers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False))

    # ### end Alembic commands ###