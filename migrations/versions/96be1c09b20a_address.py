"""address

Revision ID: 96be1c09b20a
Revises: e424a3ea740d
Create Date: 2025-07-02 13:41:13.487014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96be1c09b20a'
down_revision = 'e424a3ea740d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_number', sa.String(length=15), nullable=True))
        batch_op.add_column(sa.Column('profile_picture', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('profile_picture')
        batch_op.drop_column('phone_number')

    # ### end Alembic commands ###
