<h1 align="center">Telegram bot template✨</h1>

[![Aiogram](https://img.shields.io/badge/aiogram-3.0.0rc2-green)](https://pypi.org/project/aiogram/)
[![Python](https://img.shields.io/badge/python-3.11-green)](https://www.python.org/)

A simple telegram bot template written on the aiogram~3.0.0, using PostgreSQL and Redis databases

## 🐋 Getting start with docker

```
git clone https://github.com/aLukianov63/telegram-bot-template.git
```

Configure environment variables in ``.env`` file, see [here](#configuration)

```
docker-compose build
docker-compose up -d
```

## 💵 Payments

In order for your bot to charge users, you need to specify a [payment
token](https://core.telegram.org/bots/payments#:~:text=Getting%20a%20Token,-Use%20the%20%2Fmybots&text=Go%20to%20Bot%20Settings%20%3E%20Payments,will%20now%20show%20available%20providers.)
in the ``.env`` file

## ⚙️ Configuration

|     variables     | description                                   |
|:-----------------:|-----------------------------------------------|
|    `API_TOKEN`    | telegram bot api token                        |
|     `PG_HOST`     | hostname or an IP address PostgreSQL database |
|     `PG_PORT`     | connection port number                        |
|   `PG_PASSWORD`   | password used to authenticate                 |
|     `PG_USER`     | the username used to authenticate             |
|     `PG_NAME`     | the name of the PostgreSQL database           |
|     `RD_HOST`     | hostname or an IP address Redis database      |
|     `RD_PORT`     | port from Redis database                      |
|      `RD_DB`      | redis database number                         |
|    `PAY_TOKEN`    | your payment provider's token                 |
| `PRODUCT_1_PRICE` | product 1 price                               |
| `PRODUCT_2_PRICE` | product 2 price                               |

## 📝 License

Distributed under the MIT license. See `LICENSE` for more information.