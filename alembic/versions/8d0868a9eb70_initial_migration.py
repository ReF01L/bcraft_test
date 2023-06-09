"""initial migration

Revision ID: 8d0868a9eb70
Revises: 
Create Date: 2023-03-30 14:11:28.505852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d0868a9eb70'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('statistic',
    sa.Column('event_date', sa.Date(), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('clicks', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Float(precision=2), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('statistic')
    # ### end Alembic commands ###
