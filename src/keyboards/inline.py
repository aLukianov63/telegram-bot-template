from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton


def payment_markup() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text="1 mount plan", callback_data="1_mount_pay")
    )
    builder.row(
        InlineKeyboardButton(text="1 year plan", callback_data="1_year_pay")
    )
    return builder.as_markup()
