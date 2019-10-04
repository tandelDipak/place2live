from enum import Enum

import colorful as cf


class text_type(Enum):
    """Enum for text type."""
    WARNING = "warning"
    QUESTION = "question"
    ANSWER = "answer"


def text_color(text, txtType=None):
    """Return colored text based on text type."""
    if txtType == text_type.WARNING:
        return cf.red(text)
    if txtType == text_type.QUESTION:
        return cf.magenta(text)
    if txtType == text_type.ANSWER:
        return cf.green(text)
    return text
