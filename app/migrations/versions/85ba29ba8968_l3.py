"""l3

Revision ID: 85ba29ba8968
Revises: 0f3f13b73797
Create Date: 2025-02-12 14:55:14.192941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85ba29ba8968'
down_revision: Union[str, None] = '0f3f13b73797'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # 1. Добавляем колонку 'id' как nullable=True
    op.add_column('follows', sa.Column('id', sa.Integer(), nullable=True))

    # 2. Создаем последовательность (если её нет)
    op.execute("CREATE SEQUENCE IF NOT EXISTS follows_id_seq")

    # 3. Обновляем все записи, присваивая им значение 'id' из последовательности
    op.execute("UPDATE follows SET id = nextval('follows_id_seq')")

    # 4. Изменяем колонку 'id' на NOT NULL
    op.alter_column('follows', 'id', nullable=False)

    # 5. Устанавливаем для столбца 'id' последовательность для автоинкремента
    op.execute("ALTER TABLE follows ALTER COLUMN id SET DEFAULT nextval('follows_id_seq')")

    # 6. Добавляем ограничение уникальности на id
    op.create_unique_constraint("uq_follows_id", "follows", ["id"])

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('follows', 'id')
    # ### end Alembic commands ###
