from app.utils.helper import format_message
import os


def get_message():
    raw_message = "hello from service"
    return format_message(raw_message)


def get_secret_message():
    return os.getenv("SECRET_MESSAGE", "No secret found")