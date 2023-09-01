import asyncio

from loguru import logger

from config import Dispatcher, dispatcher, bot
from src.handlers import commands


async def on_startup() -> None:
    me = await bot.get_me()
    logger.info(f"🤖 Hello. Starting bot: {me.first_name}")


async def on_shutdown(dispatcher: Dispatcher) -> None:
    logger.info("💀 Bot finished")
    await dispatcher.storage.close()


async def main() -> None:
    logger.add("logs/info.log", level="INFO",
               format="{time} | {level} | {module}:{function}:{line} | {message}",
               rotation="10 days"
               )

    dispatcher.include_routers(
        commands.router
    )

    dispatcher.startup.register(on_startup)
    dispatcher.shutdown.register(on_shutdown)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Error run bot")
