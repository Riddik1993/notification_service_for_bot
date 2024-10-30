from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.lesson import Lesson
from database.models.subject import Subject


async def get_all_future_lessons(
        session: AsyncSession
) -> list[Lesson]:
    stmt = (
        select(Lesson)
        # .where(Lesson.lesson_dttm >= datetime.now() + timedelta(hours=24))
        # .where(Lesson.lesson_dttm < datetime.now() + timedelta(hours=25))
        .join(Subject)
        .order_by(Lesson.created_at.desc())
    )
    result = await session.execute(stmt)
    return result.scalars().all()
