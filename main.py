import asyncio
from aiogram import Bot, Dispatcher


TOKEN = "7125759779:AAFJ8kSj09MrCSwlqRy_zyNtSwqObRiMNbA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

from handless.user_privat import user_router
dp.include_router(user_router)


async def main():
    print("бот запущен")
    await dp.start_polling(bot)


asyncio.run(main())
