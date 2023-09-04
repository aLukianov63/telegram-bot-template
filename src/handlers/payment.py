from aiogram import Router, F, Bot
from aiogram.enums.currency import Currency
from aiogram.types import CallbackQuery, Message, PreCheckoutQuery
from aiogram.types.labeled_price import LabeledPrice
from loguru import logger

from config import PAY_TOKEN, PRODUCT_1_PRICE, PRODUCT_2_PRICE

router = Router()


@router.callback_query(F.data == "product_1")
async def product_1(call: CallbackQuery, bot: Bot) -> None:
    await bot.send_invoice(
        call.message.chat.id,
        title="product 1",
        description="A description of your product",
        provider_token=PAY_TOKEN,
        currency=Currency.USD,
        is_flexible=True,
        prices=[
            LabeledPrice(label="product 1", amount=PRODUCT_1_PRICE * 100),
        ],
        max_tip_amount=100000,
        suggested_tip_amounts=[5 * 100, 10 * 100, 15 * 100, 20 * 100],
        payload="product_1",
        start_parameter="",
        need_shipping_address=False,
        protect_content=False,
        reply_markup=None,
        request_timeout=15
    )


@router.callback_query(F.data == "product_2")
async def product_2(call: CallbackQuery, bot: Bot) -> None:
    await bot.send_invoice(
        call.message.chat.id,
        title="product 2",
        description="A description of your product",
        provider_token=PAY_TOKEN,
        currency=Currency.USD,
        is_flexible=True,
        prices=[
            LabeledPrice(label="product 2", amount=PRODUCT_2_PRICE * 100),
        ],
        max_tip_amount=100000,
        suggested_tip_amounts=[5 * 100, 10 * 100, 15 * 100, 20 * 100],
        payload="product_2",
        start_parameter="",
        need_shipping_address=False,
        protect_content=False,
        reply_markup=None,
        request_timeout=15
    )


@router.pre_checkout_query()
async def pre_checkout_query(pre_checkout: PreCheckoutQuery, bot: Bot) -> None:
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)


@router.message(F.successful_payment)
async def successful_payment(message: Message) -> None:
    match message.successful_payment.invoice_payload:
        case "product_1":
            await message.answer("product_1")
        case "product_2":
            await message.answer("product_1")
    logger.info(f"🤑 New payment | {message.successful_payment.invoice_payload} {message.from_user.id}")
