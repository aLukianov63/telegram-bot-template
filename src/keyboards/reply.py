from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_markup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text="🎯 Test")
    )
    builder.row(
        KeyboardButton(text="Payment 💵")
    )
    return builder.as_markup(resize_keyboard=True)
