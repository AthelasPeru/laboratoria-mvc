"""modificacion

Revision ID: 70c5db251d28
Revises: 175c80bee699
Create Date: 2016-05-20 16:52:47.319724

"""

# revision identifiers, used by Alembic.
revision = '70c5db251d28'
down_revision = '175c80bee699'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('skills', sa.Column('logo', sa.Unicode(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('skills', 'logo')
    ### end Alembic commands ###
