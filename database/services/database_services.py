from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.lesson import Lesson
from database.models.subject import Subject


async def get_all_future_lessons(
        session: AsyncSession,
        future_period_start: int,
        future_period_end: int
) -> list[Lesson]:
    current_dttm_msc = datetime.now(ZoneInfo('Europe/Paris'))

    stmt = (
        select(Lesson)
        .where(Lesson.lesson_dttm >= current_dttm_msc + timedelta(hours=future_period_start))
        .where(Lesson.lesson_dttm < current_dttm_msc + timedelta(hours=future_period_end))
        .join(Subject)
        .order_by(Lesson.created_at.desc())
    )
    result = await session.execute(stmt)
    return result.scalars().all()
