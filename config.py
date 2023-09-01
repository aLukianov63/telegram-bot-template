import os

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from dotenv import load_dotenv
from redis.asyncio.client import Redis

load_dotenv()

BOT_TOKEN = os.getenv("API_TOKEN")

PG_NAME = os.getenv("PG_NAME")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
DB_CREDITALS = [PG_NAME, PG_USER, PG_PASSWORD, PG_HOST, PG_PORT]

RD_HOST = os.getenv("RD_HOST")
RD_PORT = os.getenv("RD_PORT")
RD_DB = os.getenv("RD_DB")

redis = Redis(host=RD_HOST, port=RD_PORT, db=RD_DB)
storage = RedisStorage(redis=redis)
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dispatcher = Dispatcher(storage=storage)
