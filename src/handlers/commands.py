from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

from src.database import Database

router = Router()


@router.message(Command("start"))
async def start(message: Message, db: Database) -> None:
    tg_user = message.from_user
    app_user = await db.get_user(tg_user.id)

    if app_user is None:
        await db.new_user(tg_user.id, tg_user.username, tg_user.language_code)
        logger.info(f"😀 New user | {tg_user.id} {tg_user.username} ")

    await message.answer(f"Hello! {tg_user.username}")
