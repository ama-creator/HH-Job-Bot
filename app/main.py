from fastapi import FastAPI
from sqlalchemy import text

from app.api.v1.vacancies import router as vacancies_router
from app.db.database import async_session_maker

app = FastAPI(
    title="HH Job Bot",
    description="API for automated job search and applications",
    version="0.1.0",
)

app.include_router(vacancies_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "HH Job Bot API"}


@app.get("/health/db")
async def database_health():
    async with async_session_maker() as session:
        result = await session.execute(text("SELECT 1"))

    return {"database": result.scalar()}
