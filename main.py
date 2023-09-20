import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_read import config
from handlers import handlers
from handlers import phone_hanlders
import admin

from db.sqlite import db_start


async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_router(admin.router)
    dp.include_router(handlers.router)
    dp.include_router(phone_hanlders.router)

    await db_start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
