from zoneinfo import ZoneInfo

from database.models.lesson import Lesson
from lexicon.lexicon import LexiconRu


def render_one_lesson_text(lesson: Lesson) -> str:
    lesson_date_str = lesson.lesson_dttm.astimezone(ZoneInfo('Europe/Moscow')).strftime("%d.%m.%Y")
    lesson_time_str = lesson.lesson_dttm.astimezone(ZoneInfo('Europe/Moscow')).strftime("%H:%M")
    pointer_emoji = "✅"
    return f"{pointer_emoji} {lesson_date_str} <b>{lesson_time_str}</b> - {lesson.subject.name}"


def render_lessons_for_student(lessons: list[Lesson]) -> str:
    lessons_lst_str = [render_one_lesson_text(lesson) + "\n" for lesson in
                       lessons]
    return ''.join(lessons_lst_str)


def render_lessons_notifier_msg(lessons: list[Lesson], admin_login: str) -> str:
    lessons_lst_str = render_lessons_for_student(lessons)
    lessons_notifier_msg = LexiconRu.lesson_notification_start.value + lessons_lst_str \
                           + LexiconRu.apply_to_teacher.value + admin_login
    return lessons_notifier_msg
