from sqlalchemy import String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from tsn.database.mixins.id_mixins import IDMixin
from tsn.database.mixins.timestamps_mixins import TimestampsMixin
from tsn.database.models.base import Base


class User(IDMixin, TimestampsMixin, Base):
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(Text, unique=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)