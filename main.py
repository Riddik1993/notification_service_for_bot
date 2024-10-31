import asyncio

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from configuration import Configuration
from configuration.Configuration import load_config
from database.services.database_services import DbService
from database.services.sending_services import send_lessons_notification


async def main():
    config: Configuration = load_config()

    bot = Bot(
        token=config.telegram.token, default=DefaultBotProperties(parse_mode="HTML")
    )
    db_service = DbService(config.db.dsn)
    future_lessons = await db_service.get_all_future_lessons(24, 25)
    await send_lessons_notification(bot, future_lessons, config.telegram.admin_login)


if __name__ == "__main__":
    asyncio.run(main())
