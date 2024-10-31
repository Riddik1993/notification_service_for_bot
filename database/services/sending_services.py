from aiogram import Bot
from loguru import logger

from database.models.lesson import Lesson
from utils.rendering import render_lessons_notifier_msg


async def send_lessons_notification(bot: Bot, lessons: list[Lesson], admin_login: str):
    student_ids = [lesson.student_id for lesson in lessons]
    for student_id in student_ids:
        student_lessons = list(filter(lambda lesson: lesson.student_id == student_id, lessons))
        notification_msg = render_lessons_notifier_msg(student_lessons, admin_login)
        await bot.send_message(chat_id=student_id, text=notification_msg)
        logger.info(f"Successfully sent notification to user {student_id}")
    await bot.session.close()
