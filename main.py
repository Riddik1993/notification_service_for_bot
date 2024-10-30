import asyncio
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from configuration import Configuration
from configuration.Configuration import load_config
from database.services.lesson_services import get_all_future_lessons


async def main():
    config: Configuration = load_config()

    # bot = Bot(
    #     token=config.telegram.token, default=DefaultBotProperties(parse_mode="HTML")
    # )
    engine = create_async_engine(url=config.db.dsn)
    session_maker = async_sessionmaker(engine, expire_on_commit=False)
    async with session_maker() as session:
        future_lessons = await get_all_future_lessons(session)
        for lesson in future_lessons:
            print(lesson.lesson_dttm, lesson.subject.name, lesson.student_id)

    # await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
