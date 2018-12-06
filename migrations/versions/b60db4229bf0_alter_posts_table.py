"""alter posts table

Revision ID: b60db4229bf0
Revises: 87a4081482bc
Create Date: 2018-12-06 15:16:30.412530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b60db4229bf0'
down_revision = '87a4081482bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'user_id')
    # ### end Alembic commands ###
