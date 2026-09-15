from datetime import datetime
from enum import StrEnum

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.db.models.resume import Resume
from app.db.models.vacancy import Vacancy


class ApplicationStatus(StrEnum):
    NEW = "NEW"
    APPLIED = "APPLIED"
    NOT_VIEWED = "NOT_VIEWED"
    VIEWED = "VIEWED"
    INVITATION = "INVITATION"
    REJECTED = "REJECTED"
    WITHDRAWN = "WITHDRAWN"


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True)
    vacancy_id: Mapped[int] = mapped_column(ForeignKey("vacancies.id"), nullable=False)
    resume_id: Mapped[int] = mapped_column(ForeignKey("resumes.id"), nullable=False)
    status: Mapped[ApplicationStatus] = mapped_column(
        String(30), default=ApplicationStatus.NEW, nullable=False
    )
    cover_letter: Mapped[str | None] = mapped_column(Text, nullable=True)
    applied_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    employer_viewed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    response_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    vacancy: Mapped["Vacancy"] = relationship()
    resume: Mapped["Resume"] = relationship()
