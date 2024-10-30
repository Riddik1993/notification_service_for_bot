from zoneinfo import ZoneInfo

from database.models.lesson import Lesson
from lexicon.lexicon import LexiconRu


def render_one_lesson_text(lesson: Lesson) -> str:
    lesson_str = lesson.lesson_dttm.astimezone(ZoneInfo('Europe/Moscow')).strftime("%d.%m.%Y %H:%M")
    return f"{lesson_str} - {lesson.subject.name}"


def render_lessons_for_student(lessons: list[Lesson]) -> str:
    lessons_lst_str = [render_one_lesson_text(lesson) + "\n" for lesson in
                       lessons]
    return ''.join(lessons_lst_str)


def render_lessons_notifier_msg(lessons: list[Lesson]) -> str:
    lessons_lst_str = render_lessons_for_student(lessons)
    return LexiconRu.lesson_notification_start.value + lessons_lst_str
