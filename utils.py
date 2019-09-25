import colorful as cf
from enum import Enum

class text_type(Enum):
    WARNING = "warning"
    QUESTION = "question"
    ANSWER = "answer"

def text_color(text, type=None):
    if type == text_type.WARNING:
        return cf.red(text)
    if type == text_type.QUESTION:
        return cf.magenta(text)
    if type == text_type.ANSWER:
        return cf.green(text)
    return text