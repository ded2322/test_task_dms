"""init

Revision ID: ada38ea9178d
Revises: 
Create Date: 2024-11-28 18:06:50.610973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ada38ea9178d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reader',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reading_room',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('reading_room', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('id_reading_room', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_reading_room'], ['reading_room.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('busy_book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_book', sa.Integer(), nullable=False),
    sa.Column('id_reader', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_book'], ['book.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_reader'], ['reader.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('info_book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_book', sa.Integer(), nullable=False),
    sa.Column('id_author', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_author'], ['author.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_book'], ['book.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('info_book')
    op.drop_table('busy_book')
    op.drop_table('book')
    op.drop_table('reading_room')
    op.drop_table('reader')
    op.drop_table('author')
    # ### end Alembic commands ###
