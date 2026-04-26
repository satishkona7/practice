from app.utils.helper import format_message


def get_message():
    raw_message = "hello from service"
    return format_message(raw_message)