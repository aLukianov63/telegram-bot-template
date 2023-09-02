from aiogram import Router, F
from aiogram.types import Message

from src.keyboards.inline import payment_markup

router = Router()


@router.message(F.text == "🎯 Test")
async def start(message: Message) -> None:
    await message.answer("Test keyboard work!")


@router.message(F.text == "Payment 💵")
async def start(message: Message) -> None:
    await message.answer("choose you tariff plan", reply_markup=payment_markup())
