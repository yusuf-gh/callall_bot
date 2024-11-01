import asyncio
from aiogram import Dispatcher, Bot

from config import router

API_TOKEN = '7898591490:AAGJ3EEkeooqYXfRQSVkgD2SxOpQc4Qq5M0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
dp.include_router(router)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
