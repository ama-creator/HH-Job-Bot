from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.db.models.direction import Direction


class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    hh_resume_id: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    direction_id: Mapped[int] = mapped_column(ForeignKey("directions.id"), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    direction: Mapped["Direction"] = relationship()
