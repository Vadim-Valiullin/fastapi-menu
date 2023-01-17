"""Third

Revision ID: 722af0d2e7df
Revises: e27340051a85
Create Date: 2023-01-17 19:43:13.939404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '722af0d2e7df'
down_revision = 'e27340051a85'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Меню',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_Меню_id'), 'Меню', ['id'], unique=True)
    op.create_table('Подменю',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_Подменю_id'), 'Подменю', ['id'], unique=True)
    op.create_unique_constraint(None, 'БЛЮДА', ['title'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'БЛЮДА', type_='unique')
    op.drop_index(op.f('ix_Подменю_id'), table_name='Подменю')
    op.drop_table('Подменю')
    op.drop_index(op.f('ix_Меню_id'), table_name='Меню')
    op.drop_table('Меню')
    # ### end Alembic commands ###