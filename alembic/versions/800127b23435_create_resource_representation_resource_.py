"""Create resource, representation, resource_type tables

Revision ID: 800127b23435
Revises: 
Create Date: 2019-03-09 10:12:33.491711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '800127b23435'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'resource_type',
		sa.Column('name', sa.String(50), primary_key=True),
        sa.Column('create', sa.DateTime, nullable=False),
        sa.Column('start', sa.DateTime, nullable=True),
        sa.Column('end', sa.DateTime, nullable=True),
    )

    op.create_table(
        'resource',
        sa.Column('id', sa.Integer, primary_key=True),
		sa.Column('resource_type', sa.String(50),
				  ForeignKey('resource_type'), nullable=False)
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('create', sa.DateTime, nullable=False),
        sa.Column('start', sa.DateTime, nullable=True),
        sa.Column('end', sa.DateTime, nullable=True),
    )

    op.create_table(
        'revision',
		sa.Column('resource', sa.Integer,
				  ForeignKey('resource'), nullable=False)
		sa.Column('rev', sa.Integer, nullable=False


def downgrade():
    pass
