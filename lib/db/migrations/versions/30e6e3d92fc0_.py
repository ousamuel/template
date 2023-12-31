"""empty message

Revision ID: 30e6e3d92fc0
Revises: 
Create Date: 2023-08-09 11:05:37.939996

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30e6e3d92fc0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('day_perform', sa.String(), nullable=True),
    sa.Column('stage', sa.Integer(), nullable=True),
    sa.Column('time', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('festivals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('day_one', sa.String(), nullable=True),
    sa.Column('day_two', sa.String(), nullable=True),
    sa.Column('day_three', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('festival_artists',
    sa.Column('festival_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['festival_id'], ['festivals.id'], ),
    sa.PrimaryKeyConstraint('festival_id', 'artist_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('festival_artists')
    op.drop_table('festivals')
    op.drop_table('artists')
    # ### end Alembic commands ###
