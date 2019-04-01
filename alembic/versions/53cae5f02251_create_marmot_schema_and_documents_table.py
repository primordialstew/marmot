"""Create 'marmot' schema and documents table

Revision ID: 53cae5f02251
Revises: 
Create Date: 2019-03-30 07:21:41.402557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53cae5f02251'
down_revision = None
branch_labels = None
depends_on = None


SCHEMA_NAME = 'marmot'


def upgrade():
    op.execute("CREATE SCHEMA {schema}".format(schema=SCHEMA_NAME))
    op.create_table(
        'document',
        sa.Column('_id', sa.Integer, primary_key=True),
        sa.Column('digest_type', sa.String(50), nullable=False),
        sa.Column('digest', sa.String(50), nullable=False),
        sa.Column('document', sa.dialects.postgresql.JSONB, nullable=False),
        sa.UniqueConstraint('digest_type', 'digest'),
        sa.schema.Index('digest_idx', 'digest'),
        schema=SCHEMA_NAME,
    )


def downgrade():
    op.drop_table('document', schema=SCHEMA_NAME)
    op.execute("DROP SCHEMA {schema}".format(schema=SCHEMA_NAME))
