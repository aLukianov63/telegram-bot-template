from datetime import datetime
from typing import Optional

import asyncpg

from src.models.user import User


class Database:
    def __init__(
            self,
            name: Optional[str],
            user: Optional[str],
            password: Optional[str],
            host: Optional[str],
            port: Optional[str],
    ) -> None:
        self.pool = None

        self.name = name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    async def create_pool(self):
        self.pool = await asyncpg.create_pool(
            database=self.name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )

    async def init(self) -> None:
        with open("init.sql") as f:
            sql = f.read()
        await self.pool.execute(sql)

    async def close(self) -> None:
        await self.pool.close()

    async def new_user(self, tg_id: int, username: str, lang: str) -> None:
        await self.pool.execute("""INSERT INTO users VALUES($1, $2, $3, $4)""", tg_id, username, lang, datetime.now())

    async def get_user(self, tg_id: int) -> User:
        response = await self.pool.fetchrow("""SELECT * FROM users WHERE id=$1""", tg_id)
        if response is None:
            user = None
        else:
            user = User(response[0], response[1], response[2])
        return user
