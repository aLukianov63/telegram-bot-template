from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton


def payment_markup() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text="product 1", callback_data="product_1")
    )
    builder.row(
        InlineKeyboardButton(text="product 2", callback_data="product_2")
    )
    return builder.as_markup()
