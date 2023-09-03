<h1 align="center">Telegram bot template✨</h1>

A simple telegram bot template written on the aiogram~3.0.0, using PostgreSQL and Redis databases

## 🐋 Getting start with docker

+ ``git clone https://github.com/aLukianov63/telegram-bot-template.git``
+ configure environment variables in ``.env`` file
+ ``docker-compose build``
+ ``docker-compose up -d``

## ⚙️ Configuration

|   variables   | description                                   |
|:-------------:|-----------------------------------------------|
|  `API_TOKEN`  | telegram bot api token                        |
|   `PG_HOST`   | hostname or an IP address PostgreSQL database |
|   `PG_PORT`   | connection port number                        |
| `PG_PASSWORD` | password used to authenticate                 |
|   `PG_USER`   | the username used to authenticate             |
|   `PG_NAME`   | the name of the PostgreSQL database           |
|   `RD_HOST`   | hostname or an IP address Redis database      |
|   `RD_PORT`   | port from Redis database                      |
|    `RD_DB`    | redis database number                         |

## 📝 License

Distributed under the MIT license. See `LICENSE` for more information.