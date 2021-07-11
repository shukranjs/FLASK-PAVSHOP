"""empty message

Revision ID: 4f1cddd4a5d9
Revises: 
Create Date: 2021-07-10 22:21:43.248579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f1cddd4a5d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('price', sa.String(length=100), nullable=False),
    sa.Column('designer', sa.String(length=100), nullable=True),
    sa.Column('brand', sa.String(length=120), nullable=False),
    sa.Column('short_description', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('image', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('adress', sa.String(length=120), nullable=False),
    sa.Column('image', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('short_description', sa.String(length=127), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('published_at', sa.DateTime(), nullable=True),
    sa.Column('image', sa.String(length=20), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog')
    op.drop_table('user')
    op.drop_table('product')
    # ### end Alembic commands ###
