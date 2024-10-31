from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from database.models.lesson import Lesson
from database.models.subject import Subject
from loguru import logger


class DbService:
    def __init__(self, db_dsn: str):
        self.db_dsn = db_dsn
        engine = create_async_engine(url=self.db_dsn)
        self.session_maker = async_sessionmaker(engine, expire_on_commit=False)

    async def get_all_future_lessons(
            self,
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

        async with self.session_maker() as session:
            result = await session.execute(stmt)

            await session.close()
            future_lessons = result.scalars().all()
            logger.info(f"Get {len(future_lessons)} lessons from db to notify")
            return future_lessons
