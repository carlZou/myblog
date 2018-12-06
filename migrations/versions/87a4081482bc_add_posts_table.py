"""add posts table

Revision ID: 87a4081482bc
Revises: 7d77f8f06b00
Create Date: 2018-12-06 15:07:03.472353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87a4081482bc'
down_revision = '7d77f8f06b00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('post_body', sa.String(length=1024), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('yn', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
