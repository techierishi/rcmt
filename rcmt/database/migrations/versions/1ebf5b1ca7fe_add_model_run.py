"""Add model "Run"

Revision ID: 1ebf5b1ca7fe
Revises: b3117b16eb76
Create Date: 2022-12-17 20:49:10.111787

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "1ebf5b1ca7fe"
down_revision = "b3117b16eb76"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "runs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("checksum", sa.String(length=32), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("runs")
    # ### end Alembic commands ###
