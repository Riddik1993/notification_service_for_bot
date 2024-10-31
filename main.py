import asyncio

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

from configuration.arguments import get_arguments
from configuration.configuration import load_config, Configuration
from database.services.database_services import DbService
from database.services.sending_services import send_lessons_notification


async def main():
    config: Configuration = load_config()
    arguments = get_arguments()

    bot = Bot(
        token=config.telegram.token, default=DefaultBotProperties(parse_mode="HTML")
    )
    db_service = DbService(config.db.dsn)
    future_lessons = await db_service.get_all_future_lessons(arguments.future_hours_min, arguments.future_hours_max)
    await send_lessons_notification(bot, future_lessons, config.telegram.admin_login)


if __name__ == "__main__":
    asyncio.run(main())
