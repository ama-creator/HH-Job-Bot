from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_async_session
from app.db.models.vacancy import Vacancy
from app.schemas.vacancy import VacancyResponse

router = APIRouter(prefix="/vacancies", tags=["Vacancies"])


@router.get("/", response_model=list[VacancyResponse])
async def get_vacancies(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Vacancy))

    vacancies = result.scalars().all()
    return vacancies
