import asyncio

from loguru import logger

from config import DB_CREDITALS, Dispatcher, dispatcher, bot
from src.database import Database
from src.handlers import commands, messages, payment
from src.middlewares.db_middlewares import DatabaseMiddleware

database = Database(*DB_CREDITALS)


async def on_startup() -> None:
    try:
        await database.create_pool()
        await database.init()

        logger.info(f"🧰 Successfully created a database pool on the host: {database.host}:{database.port}")
    except Exception as e:
        logger.critical(f"🆘 Error while initing database: {e}")

    dispatcher.include_routers(
        commands.router,
        messages.router,
        payment.router
    )

    dispatcher.message.middleware.register(DatabaseMiddleware(database))

    me = await bot.get_me()
    logger.info(f"🤖 Hello. Starting bot: {me.first_name}")


async def on_shutdown(dispatcher: Dispatcher) -> None:
    logger.info("💀 Bot finished")

    await dispatcher.storage.close()
    await database.close()


async def main() -> None:
    logger.add(
        "logs/info.log",
        level="INFO",
        format="{time} | {level} | {module}:{function}:{line} | {message}",
        rotation="10 days"
    )

    dispatcher.startup.register(on_startup)
    dispatcher.shutdown.register(on_shutdown)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit) as e:
        logger.error(f"🆘Error run bot: {e}")
