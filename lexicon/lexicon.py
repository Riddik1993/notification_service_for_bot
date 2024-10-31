import enum


class LexiconRu(enum.Enum):
    emoji = "‼️"
    lesson_notification_start = f"""{emoji}Напоминание.\nУ вас запланированы следующие уроки:\n\n"""
    apply_to_teacher = "\nЕсли Вам нужно перенести или отменить занятие, пожалуйста, сообщите преподавателю:\n"
