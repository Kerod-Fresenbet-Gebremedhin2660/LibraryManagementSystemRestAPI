"""initial

Revision ID: 0d7038a197a0
Revises: 
Create Date: 2021-06-15 22:07:24.577831

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0d7038a197a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('token', sa.String(length=500), nullable=False),
                    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('token')
                    )
    op.create_table('staff',
                    sa.Column('privateId', sa.Integer(), nullable=False),
                    sa.Column('staffId', sa.Integer(), nullable=True),
                    sa.Column('email', sa.String(), nullable=True),
                    sa.Column('staffName', sa.String(length=255), nullable=False),
                    sa.Column('registered_on', sa.DateTime(), nullable=False),
                    sa.Column('hashPassword', sa.String(length=255), nullable=False),
                    sa.PrimaryKeyConstraint('privateId'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('hashPassword'),
                    sa.UniqueConstraint('staffId')
                    )
    op.create_table('student',
                    sa.Column('privateId', sa.Integer(), nullable=False),
                    sa.Column('studentId', sa.Integer(), nullable=True),
                    sa.Column('studentName', sa.String(length=255), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('sex', sa.String(), nullable=False),
                    sa.Column('dateofBirth', sa.Date(), nullable=False),
                    sa.Column('department', sa.String(length=255), nullable=False),
                    sa.Column('registered_on', sa.DateTime(), nullable=False),
                    sa.Column('password_hash', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('privateId'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('studentId')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('staff')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
