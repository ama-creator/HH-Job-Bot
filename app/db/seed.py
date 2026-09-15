import asyncio

from sqlalchemy import select

from app.db.database import async_session_maker
from app.db.models.direction import Direction

DIRECTIONS = [
    "frontend",
    "backend",
    "fullstack",
]


async def seed_directions():
    async with async_session_maker() as session:
        for name in DIRECTIONS:
            result = await session.execute(select(Direction).where(Direction.name == name))

            direction = result.scalar_one_or_none()

            if direction is None:
                session.add(Direction(name=name))

        await session.commit()


if __name__ == "__main__":
    asyncio.run(seed_directions())
